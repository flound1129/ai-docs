#!/usr/bin/env python3
"""
Fetch Meta Spatial SDK docs and convert to Markdown.

The Meta developer site embeds documentation as a double-escaped JSON
component tree in `json_cms_content`. This script extracts that tree,
parses it, and converts to markdown.

Usage:
    ./update-meta-spatial.py                    # default version v0.10.1
    ./update-meta-spatial.py --version v0.11.0  # different SDK version
    ./update-meta-spatial.py --no-push          # commit but don't push
    ./update-meta-spatial.py --no-commit        # just fetch, no git
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

BASE_URL = "https://developers.meta.com"
SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_SUBDIR = "meta-spatial-sdk"


def fetch_html(path):
    """Fetch raw HTML from a Meta developer docs page."""
    url = f"{BASE_URL}{path}"
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"    Error fetching {url}: {e}")
        return None


def get_page_links(version):
    """Get all doc page paths from the index page."""
    sdk_path = f"/horizon/reference/spatial-sdk/{version}"
    html = fetch_html(f"{sdk_path}/")
    if not html:
        return []
    pattern = rf'href="(/horizon/reference/spatial-sdk/{re.escape(version)}/[^"]+)"'
    links = re.findall(pattern, html)
    return sorted(set(links))


# ---------------------------------------------------------------------------
# JSON extraction & markdown rendering
# ---------------------------------------------------------------------------

def extract_cms_json(html):
    """Extract and parse the json_cms_content from the HTML."""
    match = re.search(r'"json_cms_content":"((?:[^"\\]|\\.)*)"', html)
    if not match:
        return None

    raw = match.group(1)
    unescaped = raw.replace('\\"', '"').replace('\\\\', '\\')

    try:
        return json.loads(unescaped)
    except json.JSONDecodeError:
        try:
            unescaped2 = unescaped.replace('\\"', '"').replace('\\/', '/')
            return json.loads(unescaped2)
        except json.JSONDecodeError as e:
            print(f"    JSON parse error: {e}")
            return None


def render_node(node):
    """Recursively render a component tree node to markdown lines."""
    if isinstance(node, str):
        text = node.replace('\\n', '\n').strip()
        return [text] if text else []

    if isinstance(node, list):
        lines = []
        for child in node:
            lines.extend(render_node(child))
        return lines

    if not isinstance(node, dict):
        return []

    ntype = node.get("type", "")
    children = node.get("children", [])
    props = node.get("props", {})

    if ntype == "DMCCommonH1":
        return [f"# {collect_text(children)}", ""]
    if ntype == "DMCCommonH2":
        return [f"## {collect_text(children)}", ""]
    if ntype == "DMCCommonH3":
        return [f"### {collect_text(children)}", ""]

    if ntype == "DMCCommonP":
        text = collect_inline(children)
        return [text.strip(), ""] if text.strip() else []

    if ntype == "DMCuiCodeBlock":
        code = collect_text(children).strip()
        return ["```kotlin", code, "```", ""] if code else []

    if ntype == "DMCCommonCode":
        return [f"`{collect_text(children)}`"]

    if ntype == "GalaxySharedB":
        return [f"**{collect_text(children)}**"]

    if ntype == "GalaxySharedI":
        text = collect_text(children).strip()
        return [f"*{text}*", ""] if text else []

    if ntype == "DEVHorizonA":
        href = props.get("href", "")
        return [f"[{collect_text(children)}]({href})"]

    if ntype == "DMCCommonTable":
        return render_table(children)
    if ntype == "DMCCommonTr":
        return render_table_row(children)

    if ntype == "DMCCommonLi":
        return [f"- {collect_inline(children).strip()}"]

    if ntype == "DMCCommonUl":
        lines = []
        for child in children:
            lines.extend(render_node(child))
        lines.append("")
        return lines

    # Container nodes - recurse
    if ntype in ("DMCCommonDiv", "Fragment", "MCDSCMSCommonText",
                 "MCDSCMSCommonBox", "GalaxyHTMLSpan", "DMCCommonTd",
                 "DMCCommonTh", "DMCCommonThead", "DMCCommonTbody",
                 "DMCCommonSpan"):
        lines = []
        for child in children:
            lines.extend(render_node(child))
        return lines

    # Unknown type - recurse
    if children:
        lines = []
        for child in children:
            lines.extend(render_node(child))
        return lines

    return []


def collect_text(children):
    """Collect all plain text from children, ignoring formatting."""
    parts = []
    if isinstance(children, str):
        return children.replace('\\n', ' ').strip()
    if isinstance(children, list):
        for child in children:
            if isinstance(child, str):
                parts.append(child.replace('\\n', ' ').strip())
            elif isinstance(child, dict):
                parts.append(collect_text(child.get("children", [])))
    return " ".join(p for p in parts if p)


def collect_inline(children):
    """Collect inline content preserving formatting (code, bold, links)."""
    parts = []
    if isinstance(children, str):
        return children.replace('\\n', '\n').strip()
    if isinstance(children, list):
        for child in children:
            if isinstance(child, str):
                text = child.replace('\\n', ' ').strip()
                if text:
                    parts.append(text)
            elif isinstance(child, dict):
                parts.extend(render_node(child))
    return " ".join(p for p in parts if p)


def render_table(children):
    """Render a table node to markdown."""
    rows = []
    for child in children:
        if isinstance(child, dict):
            ntype = child.get("type", "")
            if ntype in ("DMCCommonThead", "DMCCommonTbody"):
                for subchild in child.get("children", []):
                    if isinstance(subchild, dict) and subchild.get("type") == "DMCCommonTr":
                        rows.append(render_table_row_cells(subchild.get("children", [])))
            elif ntype == "DMCCommonTr":
                rows.append(render_table_row_cells(child.get("children", [])))

    if not rows:
        return []

    lines = []
    header = rows[0]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join(["---"] * len(header)) + " |")
    for row in rows[1:]:
        while len(row) < len(header):
            row.append("")
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")
    return lines


def render_table_row_cells(children):
    """Extract cell contents from a table row's children."""
    cells = []
    for child in children:
        if isinstance(child, dict):
            ntype = child.get("type", "")
            if ntype in ("DMCCommonTd", "DMCCommonTh"):
                text = collect_inline(child.get("children", []))
                text = re.sub(r'\s+', ' ', text).strip()
                cells.append(text)
    return cells


def render_table_row(children):
    """Render a single table row (fallback)."""
    cells = render_table_row_cells(children)
    return ["| " + " | ".join(cells) + " |"] if cells else []


def convert_page(html):
    """Convert a page's HTML to markdown."""
    if not html:
        return None
    tree = extract_cms_json(html)
    if not tree:
        return None

    title_match = re.search(
        r'<meta\s+property="og:title"\s+content="([^"]*)"', html
    )
    fallback_title = title_match.group(1) if title_match else None
    if fallback_title:
        fallback_title = re.sub(r'\s*\|.*$', '', fallback_title)

    lines = render_node(tree)

    result = "\n".join(lines)
    result = re.sub(r'\n{3,}', '\n\n', result)
    result = result.replace('\\/', '/')
    result = result.strip()

    if result and not result.startswith("# ") and fallback_title:
        result = f"# {fallback_title}\n\n{result}"
    elif not result and fallback_title:
        result = f"# {fallback_title}\n"

    return result if result else None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def git_commit_and_push(push=True):
    """Stage all changes, commit if there are diffs, and optionally push."""
    os.chdir(SCRIPT_DIR)
    subprocess.run(["git", "add", "-A"], check=True)

    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        capture_output=True,
    )
    if result.returncode == 0:
        print("\nNo changes detected — docs are already up to date.")
        return

    subprocess.run(
        ["git", "commit", "-m", "Update Meta Spatial SDK documentation"],
        check=True,
    )

    if push:
        print("\nPushing to remote...")
        subprocess.run(["git", "push"], check=True)
        print("Pushed.")
    else:
        print("\nCommitted locally (--no-push).")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Meta Spatial SDK docs and convert to Markdown.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
examples:
  ./update-meta-spatial.py                      # default: v0.10.1
  ./update-meta-spatial.py --version v0.11.0    # different version
  ./update-meta-spatial.py --no-push            # commit but don't push
  ./update-meta-spatial.py --no-commit          # just fetch, no git
""",
    )
    parser.add_argument(
        "--version", default="v0.10.1",
        help="SDK version to fetch (default: v0.10.1)",
    )
    parser.add_argument(
        "--no-push", action="store_true",
        help="Commit but don't push to remote",
    )
    parser.add_argument(
        "--no-commit", action="store_true",
        help="Just fetch docs, skip git commit and push",
    )
    args = parser.parse_args()

    out_dir = SCRIPT_DIR / OUTPUT_SUBDIR
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Meta Spatial SDK Documentation Scraper")
    print(f"  Version: {args.version}")
    print("=" * 60)

    print("\nFetching page index...")
    links = get_page_links(args.version)
    print(f"Found {len(links)} documentation pages")

    if not links:
        print("No pages found!")
        return

    total = 0
    errors = 0

    for i, link in enumerate(links, 1):
        slug = link.rstrip("/").split("/")[-1]
        print(f"  [{i}/{len(links)}] {slug}...", end=" ", flush=True)

        html = fetch_html(link)
        if not html:
            errors += 1
            print("FAILED (fetch)")
            time.sleep(0.3)
            continue

        md = convert_page(html)
        if md and len(md) > 20:
            filepath = out_dir / f"{slug}.md"
            filepath.write_text(md, encoding="utf-8")
            total += 1
            print("ok")
        else:
            errors += 1
            print("FAILED (parse)")

        time.sleep(0.3)

    print(f"\nDone! Saved {total} pages, {errors} errors.")

    if not args.no_commit:
        git_commit_and_push(push=not args.no_push)

    print(f"\nAll documentation saved to: {out_dir}")


if __name__ == "__main__":
    main()
