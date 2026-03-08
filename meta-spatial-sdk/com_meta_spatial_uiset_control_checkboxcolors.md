# CheckboxColors Class

*Modifiers:
final*

Represents the colors used by the three different sections (checkmark, box, and border) of a [null.SpatialCheckbox](/reference/spatial-sdk/v0.10.1/null#spatialcheckbox) in different states.

## Constructors

| **CheckboxColors** ( checkedCheckmarkColor , uncheckedCheckmarkColor , checkedBoxColor , uncheckedBoxColor , disabledCheckedBoxColor , disabledUncheckedBoxColor , disabledIndeterminateBoxColor , checkedBorderColor , uncheckedBorderColor , disabledBorderColor , disabledUncheckedBorderColor , disabledIndeterminateBorderColor ) | create an instance with arbitrary colors, see [CheckboxDefaults.colors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_checkboxdefaults#colors) for the default implementation. Signature ```kotlin constructor(checkedCheckmarkColor: Color, uncheckedCheckmarkColor: Color, checkedBoxColor: Color, uncheckedBoxColor: Color, disabledCheckedBoxColor: Color, disabledUncheckedBoxColor: Color, disabledIndeterminateBoxColor: Color, checkedBorderColor: Color, uncheckedBorderColor: Color, disabledBorderColor: Color, disabledUncheckedBorderColor: Color, disabledIndeterminateBorderColor: Color) ``` Parameters checkedCheckmarkColor: Color color that will be used for the checkmark when checked uncheckedCheckmarkColor: Color color that will be used for the checkmark when unchecked checkedBoxColor: Color the color that will be used for the box when checked uncheckedBoxColor: Color color that will be used for the box when unchecked disabledCheckedBoxColor: Color color that will be used for the box when disabled and checked disabledUncheckedBoxColor: Color color that will be used for the box when disabled and unchecked disabledIndeterminateBoxColor: Color color that will be used for the box and border in a [null.SpatialCheckbox](/reference/spatial-sdk/v0.10.1/null#spatialcheckbox) when disabled AND in an ToggleableState.Indeterminate state. checkedBorderColor: Color color that will be used for the border when checked uncheckedBorderColor: Color color that will be used for the border when unchecked disabledBorderColor: Color color that will be used for the border when disabled and checked disabledUncheckedBorderColor: Color color that will be used for the border when disabled and unchecked disabledIndeterminateBorderColor: Color color that will be used for the border when disabled and in an ToggleableState.Indeterminate state. Returns [CheckboxColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_checkboxcolors) |
| --- | --- |

## Properties

| **checkedBorderColor** : Color [Get] | Signature ```kotlin val checkedBorderColor: Color ``` |
| --- | --- |
| **checkedBoxColor** : Color [Get] | Signature ```kotlin val checkedBoxColor: Color ``` |
| **checkedCheckmarkColor** : Color [Get] | Signature ```kotlin val checkedCheckmarkColor: Color ``` |
| **disabledBorderColor** : Color [Get] | Signature ```kotlin val disabledBorderColor: Color ``` |
| **disabledCheckedBoxColor** : Color [Get] | Signature ```kotlin val disabledCheckedBoxColor: Color ``` |
| **disabledIndeterminateBorderColor** : Color [Get] | Signature ```kotlin val disabledIndeterminateBorderColor: Color ``` |
| **disabledIndeterminateBoxColor** : Color [Get] | Signature ```kotlin val disabledIndeterminateBoxColor: Color ``` |
| **disabledUncheckedBorderColor** : Color [Get] | Signature ```kotlin val disabledUncheckedBorderColor: Color ``` |
| **disabledUncheckedBoxColor** : Color [Get] | Signature ```kotlin val disabledUncheckedBoxColor: Color ``` |
| **uncheckedBorderColor** : Color [Get] | Signature ```kotlin val uncheckedBorderColor: Color ``` |
| **uncheckedBoxColor** : Color [Get] | Signature ```kotlin val uncheckedBoxColor: Color ``` |
| **uncheckedCheckmarkColor** : Color [Get] | Signature ```kotlin val uncheckedCheckmarkColor: Color ``` |

## Functions

| **copy** ( checkedCheckmarkColor , uncheckedCheckmarkColor , checkedBoxColor , uncheckedBoxColor , disabledCheckedBoxColor , disabledUncheckedBoxColor , disabledIndeterminateBoxColor , checkedBorderColor , uncheckedBorderColor , disabledBorderColor , disabledUncheckedBorderColor , disabledIndeterminateBorderColor ) | Returns a copy of this CheckboxColors, optionally overriding some of the values. This uses the Color.Unspecified to mean “use the value from the source” Signature ```kotlin fun copy(checkedCheckmarkColor: Color, uncheckedCheckmarkColor: Color, checkedBoxColor: Color, uncheckedBoxColor: Color, disabledCheckedBoxColor: Color, disabledUncheckedBoxColor: Color, disabledIndeterminateBoxColor: Color, checkedBorderColor: Color, uncheckedBorderColor: Color, disabledBorderColor: Color, disabledUncheckedBorderColor: Color, disabledIndeterminateBorderColor: Color): CheckboxColors ``` Parameters checkedCheckmarkColor: Color uncheckedCheckmarkColor: Color checkedBoxColor: Color uncheckedBoxColor: Color disabledCheckedBoxColor: Color disabledUncheckedBoxColor: Color disabledIndeterminateBoxColor: Color checkedBorderColor: Color uncheckedBorderColor: Color disabledBorderColor: Color disabledUncheckedBorderColor: Color disabledIndeterminateBorderColor: Color Returns [CheckboxColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_checkboxcolors) |
| --- | --- |
| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |