# SwitchColors Class

*Modifiers:
final*

Represents the colors used by a [null.SpatialSwitch](/reference/spatial-sdk/v0.10.1/null#spatialswitch) in different states

## Constructors

| **SwitchColors** ( checkedThumbColor , checkedTrackColor , checkedBorderColor , checkedIconColor , uncheckedThumbColor , uncheckedTrackColor , uncheckedBorderColor , uncheckedIconColor , disabledCheckedThumbColor , disabledCheckedTrackColor , disabledCheckedBorderColor , disabledCheckedIconColor , disabledUncheckedThumbColor , disabledUncheckedTrackColor , disabledUncheckedBorderColor , disabledUncheckedIconColor ) | create an instance with arbitrary colors. See [SwitchDefaults.colors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_switchdefaults#colors) for the default implementation. Signature ```kotlin constructor(checkedThumbColor: Color, checkedTrackColor: Color, checkedBorderColor: Color, checkedIconColor: Color, uncheckedThumbColor: Color, uncheckedTrackColor: Color, uncheckedBorderColor: Color, uncheckedIconColor: Color, disabledCheckedThumbColor: Color, disabledCheckedTrackColor: Color, disabledCheckedBorderColor: Color, disabledCheckedIconColor: Color, disabledUncheckedThumbColor: Color, disabledUncheckedTrackColor: Color, disabledUncheckedBorderColor: Color, disabledUncheckedIconColor: Color) ``` Parameters checkedThumbColor: Color the color used for the thumb when enabled and checked checkedTrackColor: Color the color used for the track when enabled and checked checkedBorderColor: Color the color used for the border when enabled and checked checkedIconColor: Color the color used for the icon when enabled and checked uncheckedThumbColor: Color the color used for the thumb when enabled and unchecked uncheckedTrackColor: Color the color used for the track when enabled and unchecked uncheckedBorderColor: Color the color used for the border when enabled and unchecked uncheckedIconColor: Color the color used for the icon when enabled and unchecked disabledCheckedThumbColor: Color the color used for the thumb when disabled and checked disabledCheckedTrackColor: Color the color used for the track when disabled and checked disabledCheckedBorderColor: Color the color used for the border when disabled and checked disabledCheckedIconColor: Color the color used for the icon when disabled and checked disabledUncheckedThumbColor: Color the color used for the thumb when disabled and unchecked disabledUncheckedTrackColor: Color the color used for the track when disabled and unchecked disabledUncheckedBorderColor: Color the color used for the border when disabled and unchecked disabledUncheckedIconColor: Color the color used for the icon when disabled and unchecked Returns [SwitchColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_switchcolors) |
| --- | --- |

## Properties

| **checkedBorderColor** : Color [Get] | Signature ```kotlin val checkedBorderColor: Color ``` |
| --- | --- |
| **checkedIconColor** : Color [Get] | Signature ```kotlin val checkedIconColor: Color ``` |
| **checkedThumbColor** : Color [Get] | Signature ```kotlin val checkedThumbColor: Color ``` |
| **checkedTrackColor** : Color [Get] | Signature ```kotlin val checkedTrackColor: Color ``` |
| **disabledCheckedBorderColor** : Color [Get] | Signature ```kotlin val disabledCheckedBorderColor: Color ``` |
| **disabledCheckedIconColor** : Color [Get] | Signature ```kotlin val disabledCheckedIconColor: Color ``` |
| **disabledCheckedThumbColor** : Color [Get] | Signature ```kotlin val disabledCheckedThumbColor: Color ``` |
| **disabledCheckedTrackColor** : Color [Get] | Signature ```kotlin val disabledCheckedTrackColor: Color ``` |
| **disabledUncheckedBorderColor** : Color [Get] | Signature ```kotlin val disabledUncheckedBorderColor: Color ``` |
| **disabledUncheckedIconColor** : Color [Get] | Signature ```kotlin val disabledUncheckedIconColor: Color ``` |
| **disabledUncheckedThumbColor** : Color [Get] | Signature ```kotlin val disabledUncheckedThumbColor: Color ``` |
| **disabledUncheckedTrackColor** : Color [Get] | Signature ```kotlin val disabledUncheckedTrackColor: Color ``` |
| **uncheckedBorderColor** : Color [Get] | Signature ```kotlin val uncheckedBorderColor: Color ``` |
| **uncheckedIconColor** : Color [Get] | Signature ```kotlin val uncheckedIconColor: Color ``` |
| **uncheckedThumbColor** : Color [Get] | Signature ```kotlin val uncheckedThumbColor: Color ``` |
| **uncheckedTrackColor** : Color [Get] | Signature ```kotlin val uncheckedTrackColor: Color ``` |

## Functions

| **copy** ( checkedThumbColor , checkedTrackColor , checkedBorderColor , checkedIconColor , uncheckedThumbColor , uncheckedTrackColor , uncheckedBorderColor , uncheckedIconColor , disabledCheckedThumbColor , disabledCheckedTrackColor , disabledCheckedBorderColor , disabledCheckedIconColor , disabledUncheckedThumbColor , disabledUncheckedTrackColor , disabledUncheckedBorderColor , disabledUncheckedIconColor ) | Returns a copy of this SwitchColors, optionally overriding some of the values. This uses the Color.Unspecified to mean “use the value from the source” Signature ```kotlin fun copy(checkedThumbColor: Color, checkedTrackColor: Color, checkedBorderColor: Color, checkedIconColor: Color, uncheckedThumbColor: Color, uncheckedTrackColor: Color, uncheckedBorderColor: Color, uncheckedIconColor: Color, disabledCheckedThumbColor: Color, disabledCheckedTrackColor: Color, disabledCheckedBorderColor: Color, disabledCheckedIconColor: Color, disabledUncheckedThumbColor: Color, disabledUncheckedTrackColor: Color, disabledUncheckedBorderColor: Color, disabledUncheckedIconColor: Color): SwitchColors ``` Parameters checkedThumbColor: Color checkedTrackColor: Color checkedBorderColor: Color checkedIconColor: Color uncheckedThumbColor: Color uncheckedTrackColor: Color uncheckedBorderColor: Color uncheckedIconColor: Color disabledCheckedThumbColor: Color disabledCheckedTrackColor: Color disabledCheckedBorderColor: Color disabledCheckedIconColor: Color disabledUncheckedThumbColor: Color disabledUncheckedTrackColor: Color disabledUncheckedBorderColor: Color disabledUncheckedIconColor: Color Returns [SwitchColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_switchcolors) |
| --- | --- |
| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |