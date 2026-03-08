# SpatialSideNavItem Function

*Modifiers:
final*

A single item in a side navigation menu.

## Signature

```kotlin
fun SpatialSideNavItem(icon: () -> Unit, onClick: () -> Unit, primaryLabel: String, modifier: Modifier, interactionSource: MutableInteractionSource) }, secondaryLabel: String? = null, collapsed: Boolean = false, dense: Boolean = false, showExpandedIcon: Boolean = true, selected: Boolean = false, colors: SideNavItemColors = SideNavItemDefaults.colors(), primaryTextStyle: TextStyle, secondaryTextStyle: TextStyle, selectedBackgroundColor: Color?)
```

## Parameters

icon:
Function0
A composable function that represents the icon of the item.
onClick:
Function0
Callback invoked when the item is clicked.
primaryLabel:
String
The primary label text of the item.
modifier:
Modifier
Modifier to be applied to the item.
interactionSource:
MutableInteractionSource
The interaction source for the clickable behavior.
secondaryLabel:
String?
The secondary label text of the item (optional).
collapsed:
Boolean
Whether the side navigation is collapsed or expanded.
dense:
Boolean
Whether the item should be displayed in a dense format.
showExpandedIcon:
Boolean
Whether to show the icon when expanded.
selected:
Boolean
Whether the item is selected or not.
colors:
[SideNavItemColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_navigation_foundation_sidenavitemcolors)
The colors to use for different states of the item.
primaryTextStyle:
TextStyle
The TextStyle to be used for the primary label.
secondaryTextStyle:
TextStyle
The TextStyle to be used for the secondary label.
selectedBackgroundColor:
Color?
The background color to use when the item is selected. Defaults to null, which uses the default background color.