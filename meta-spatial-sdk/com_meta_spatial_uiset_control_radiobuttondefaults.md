# RadioButtonDefaults Object

Defaults used in [null.SpatialRadioButton](/reference/spatial-sdk/v0.10.1/null#spatialradiobutton) .

## Signature

```kotlin
object RadioButtonDefaults
```

## Functions

| **colors** () | Creates a [RadioButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_radiobuttoncolors) that will animate between the provided colors. Signature ```kotlin fun colors(): RadioButtonColors ``` Returns [RadioButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_radiobuttoncolors) |
| --- | --- |
| **colors** ( selectedColor , selectedDotColor , unselectedColor , disabledSelectedColor , disabledSelectedDotColor , disabledUnselectedColor ) | Creates a [RadioButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_radiobuttoncolors) that will animate between the provided colors. Signature ```kotlin fun colors(selectedColor: Color, selectedDotColor: Color, unselectedColor: Color, disabledSelectedColor: Color, disabledSelectedDotColor: Color, disabledUnselectedColor: Color): RadioButtonColors ``` Parameters selectedColor: Color the color to use for the RadioButton when selected and enabled. selectedDotColor: Color the color to use for the RadioButton's inner dot when selected and enabled. unselectedColor: Color the color to use for the RadioButton when unselected and enabled. disabledSelectedColor: Color the color to use for the RadioButton when disabled and selected. disabledSelectedDotColor: Color the color to use for the RadioButton's inner dot when disabled and selected. disabledUnselectedColor: Color the color to use for the RadioButton when disabled and not selected. Returns [RadioButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_radiobuttoncolors) the resulting [RadioButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_radiobuttoncolors) used for the RadioButton |