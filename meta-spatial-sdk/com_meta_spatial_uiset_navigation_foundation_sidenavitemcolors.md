# SideNavItemColors Class

*Modifiers:
final*

Represents the color used by a [null.SpatialSideNavItem](/reference/spatial-sdk/v0.10.1/null#spatialsidenavitem) in different states.

## Constructors

| **SideNavItemColors** ( selectedBackgroundColor , selectedPrimaryColor , selectedSecondaryColor , unselectedBackgroundColor , unselectedPrimaryColor , unselectedSecondaryColor ) | create an instance with arbitrary colors. See [SideNavItemDefaults.colors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_navigation_foundation_sidenavitemdefaults#colors) for the default implementation. Signature ```kotlin constructor(selectedBackgroundColor: Color, selectedPrimaryColor: Color, selectedSecondaryColor: Color, unselectedBackgroundColor: Color, unselectedPrimaryColor: Color, unselectedSecondaryColor: Color) ``` Parameters selectedBackgroundColor: Color the color to use for the RadioButton when selected and enabled. selectedPrimaryColor: Color the color to use for the RadioButton's inner dot when selected and enabled. selectedSecondaryColor: Color the color to use for the RadioButton when unselected and enabled. unselectedBackgroundColor: Color the color to use for the RadioButton when disabled and selected. unselectedPrimaryColor: Color the color to use for the RadioButton's inner dot when disabled and selected. unselectedSecondaryColor: Color the color to use for the RadioButton when disabled and not selected. Returns [SideNavItemColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_navigation_foundation_sidenavitemcolors) |
| --- | --- |

## Properties

| **selectedBackgroundColor** : Color [Get] | Signature ```kotlin val selectedBackgroundColor: Color ``` |
| --- | --- |
| **selectedPrimaryColor** : Color [Get] | Signature ```kotlin val selectedPrimaryColor: Color ``` |
| **selectedSecondaryColor** : Color [Get] | Signature ```kotlin val selectedSecondaryColor: Color ``` |
| **unselectedBackgroundColor** : Color [Get] | Signature ```kotlin val unselectedBackgroundColor: Color ``` |
| **unselectedPrimaryColor** : Color [Get] | Signature ```kotlin val unselectedPrimaryColor: Color ``` |
| **unselectedSecondaryColor** : Color [Get] | Signature ```kotlin val unselectedSecondaryColor: Color ``` |

## Functions

| **copy** ( selectedBackgroundColor , selectedPrimaryColor , selectedSecondaryColor , unselectedBackgroundColor , unselectedPrimaryColor , unselectedSecondaryColor ) | Returns a copy of this RadioButtonColors, optionally overriding some of the values. This uses the Color.Unspecified to mean “use the value from the source” Signature ```kotlin fun copy(selectedBackgroundColor: Color, selectedPrimaryColor: Color, selectedSecondaryColor: Color, unselectedBackgroundColor: Color, unselectedPrimaryColor: Color, unselectedSecondaryColor: Color): SideNavItemColors ``` Parameters selectedBackgroundColor: Color selectedPrimaryColor: Color selectedSecondaryColor: Color unselectedBackgroundColor: Color unselectedPrimaryColor: Color unselectedSecondaryColor: Color Returns [SideNavItemColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_navigation_foundation_sidenavitemcolors) |
| --- | --- |
| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |