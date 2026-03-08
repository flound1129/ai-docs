# RadioButtonColors Class

*Modifiers:
final*

Represents the color used by a [null.SpatialRadioButton](/reference/spatial-sdk/v0.10.1/null#spatialradiobutton) in different states.

## Constructors

| **RadioButtonColors** ( selectedColor , selectedDotColor , unselectedColor , disabledSelectedColor , disabledSelectedDotColor , disabledUnselectedColor ) | create an instance with arbitrary colors. See [RadioButtonDefaults.colors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_radiobuttondefaults#colors) for the default implementation. Signature ```kotlin constructor(selectedColor: Color, selectedDotColor: Color, unselectedColor: Color, disabledSelectedColor: Color, disabledSelectedDotColor: Color, disabledUnselectedColor: Color) ``` Parameters selectedColor: Color the color to use for the RadioButton when selected and enabled. selectedDotColor: Color the color to use for the RadioButton's inner dot when selected and enabled. unselectedColor: Color the color to use for the RadioButton when unselected and enabled. disabledSelectedColor: Color the color to use for the RadioButton when disabled and selected. disabledSelectedDotColor: Color the color to use for the RadioButton's inner dot when disabled and selected. disabledUnselectedColor: Color the color to use for the RadioButton when disabled and not selected. Returns [RadioButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_radiobuttoncolors) |
| --- | --- |

## Properties

| **disabledSelectedColor** : Color [Get] | Signature ```kotlin val disabledSelectedColor: Color ``` |
| --- | --- |
| **disabledSelectedDotColor** : Color [Get] | Signature ```kotlin val disabledSelectedDotColor: Color ``` |
| **disabledUnselectedColor** : Color [Get] | Signature ```kotlin val disabledUnselectedColor: Color ``` |
| **selectedColor** : Color [Get] | Signature ```kotlin val selectedColor: Color ``` |
| **selectedDotColor** : Color [Get] | Signature ```kotlin val selectedDotColor: Color ``` |
| **unselectedColor** : Color [Get] | Signature ```kotlin val unselectedColor: Color ``` |

## Functions

| **copy** ( selectedColor , selectedDotColor , unselectedColor , disabledSelectedColor , disabledSelectedDotColor , disabledUnselectedColor ) | Returns a copy of this RadioButtonColors, optionally overriding some of the values. This uses the Color.Unspecified to mean “use the value from the source” Signature ```kotlin fun copy(selectedColor: Color, selectedDotColor: Color, unselectedColor: Color, disabledSelectedColor: Color, disabledSelectedDotColor: Color, disabledUnselectedColor: Color): RadioButtonColors ``` Parameters selectedColor: Color selectedDotColor: Color unselectedColor: Color disabledSelectedColor: Color disabledSelectedDotColor: Color disabledUnselectedColor: Color Returns [RadioButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_radiobuttoncolors) |
| --- | --- |
| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |