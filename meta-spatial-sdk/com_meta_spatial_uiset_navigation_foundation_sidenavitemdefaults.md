# SideNavItemDefaults Object

Defaults used in [null.SpatialSideNavItem](/reference/spatial-sdk/v0.10.1/null#spatialsidenavitem) .

## Signature

```kotlin
object SideNavItemDefaults
```

## Functions

| **colors** () | Creates a [null.SpatialSideNavItem](/reference/spatial-sdk/v0.10.1/null#spatialsidenavitem) that will animate between the provided colors. Signature ```kotlin fun colors(): SideNavItemColors ``` Returns [SideNavItemColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_navigation_foundation_sidenavitemcolors) |
| --- | --- |
| **colors** ( selectedBackgroundColor , selectedPrimaryColor , selectedSecondaryColor , unselectedBackgroundColor , unselectedPrimaryColor , unselectedSecondaryColor ) | Creates a [null.SpatialSideNavItem](/reference/spatial-sdk/v0.10.1/null#spatialsidenavitem) that will animate between the provided colors. Signature ```kotlin fun colors(selectedBackgroundColor: Color, selectedPrimaryColor: Color, selectedSecondaryColor: Color, unselectedBackgroundColor: Color, unselectedPrimaryColor: Color, unselectedSecondaryColor: Color): SideNavItemColors ``` Parameters selectedBackgroundColor: Color the color to use for the RadioButton when selected and enabled. selectedPrimaryColor: Color the color to use for the RadioButton's inner dot when selected and enabled. selectedSecondaryColor: Color the color to use for the RadioButton when unselected and enabled. unselectedBackgroundColor: Color the color to use for the RadioButton when disabled and selected. unselectedPrimaryColor: Color the color to use for the RadioButton's inner dot when disabled and selected. unselectedSecondaryColor: Color the color to use for the RadioButton when disabled and not selected. Returns [SideNavItemColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_navigation_foundation_sidenavitemcolors) the resulting [SideNavItemColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_navigation_foundation_sidenavitemcolors) used for the RadioButton |