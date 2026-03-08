# SpatialDropdown Function

*Modifiers:
final*

Dropdowns group multiple options under a single header and display the active selection. They keep items hidden until the user clicks the primary chevron. This offers a neat way to manage numerous options within one component.

## Signature

```kotlin
fun SpatialDropdown(items: List<SpatialDropdownItem>, onItemSelected: (SpatialDropdownItem) -> Unit, modifier: Modifier, filled: Boolean = true, leading: () -> Unit? = null, title: String? = null, subtitle: String? = null, enabled: Boolean = true, selectedItem: SpatialDropdownItem? = null, showChevron: Boolean = true, menuModifier: Modifier, showDividers: Boolean = false)
```

## Parameters

items:
List
The list of items to be displayed in the dropdown.
onItemSelected:
Function1
The callback to be invoked when an item is selected.
modifier:
Modifier
The Modifier to be applied to this dropdown.
filled:
Boolean
Whether the dropdown is filled or not. Defaults to true.
leading:
Function0?
A composable function that provides the leading icon for the dropdown.
title:
String?
The title text of the dropdown.
subtitle:
String?
The subtitle text of the dropdown.
enabled:
Boolean
Whether the dropdown is enabled or disabled.
selectedItem:
[SpatialDropdownItem?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_dropdown_foundation_spatialdropdownitem)
The currently selected item in the dropdown.
showChevron:
Boolean
Whether to show the chevron, in the case of a pill variant. Defaults to true.
menuModifier:
Modifier
The Modifier to be applied to the menu.
showDividers:
Boolean
Whether to show dividers between items. Defaults to false.