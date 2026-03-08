# SpatialIconDropdown Function

*Modifiers:
final*

Icon dropdowns are a variant of dropdowns that display an icon instead of a title. They are useful when the dropdown is used in a context where the icon is more relevant than the text.

## Signature

```kotlin
fun SpatialIconDropdown(icon: () -> Unit, items: List<SpatialDropdownItem>, onItemSelected: (SpatialDropdownItem) -> Unit, modifier: Modifier, filled: Boolean = true, enabled: Boolean = true, selectedItem: SpatialDropdownItem? = null, showChevron: Boolean = true, menuModifier: Modifier, showDividers: Boolean = false)
```

## Parameters

icon:
Function0
A composable function that provides the icon for the dropdown.
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