# SpatialTooltip Function

*Modifiers:
final*

Displays an anchor Composable that shows a tooltip when hovered.

## Signature

```kotlin
fun SpatialTooltip(title: String, subtitle: String? = null, icon: () -> Unit? = null, anchor: () -> Unit, alignment: Alignment, offset: IntOffset, -100), interactionSource: MutableInteractionSource) })
```

## Parameters

title:
String
The title to display inside the tooltip.
subtitle:
String?
Optional subtitle.
icon:
Function0?
Optional icon displayed to the left of the text.
anchor:
Function0
The Composable that acts as the hover target.
alignment:
Alignment
Alignment of the tooltip relative to the anchor.
offset:
IntOffset
Offset of the tooltip relative to the anchor.
interactionSource:
MutableInteractionSource