# CheckboxDefaults Object

Defaults used in [null.SpatialCheckbox](/reference/spatial-sdk/v0.10.1/null#spatialcheckbox) .

## Signature

```kotlin
object CheckboxDefaults
```

## Functions

| **colors** () | Creates a [CheckboxColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_checkboxcolors) that will animate between the provided colors. Signature ```kotlin fun colors(): CheckboxColors ``` Returns [CheckboxColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_checkboxcolors) |
| --- | --- |
| **colors** ( checkedColor , uncheckedColor , checkmarkColor , disabledCheckedColor , disabledUncheckedColor , disabledIndeterminateColor ) | Creates a [CheckboxColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_checkboxcolors) that will animate between the provided colors. Signature ```kotlin fun colors(checkedColor: Color, uncheckedColor: Color, checkmarkColor: Color, disabledCheckedColor: Color, disabledUncheckedColor: Color, disabledIndeterminateColor: Color): CheckboxColors ``` Parameters checkedColor: Color the color that will be used for the border and box when checked uncheckedColor: Color color that will be used for the border when unchecked. By default, the inner box is transparent when unchecked. checkmarkColor: Color color that will be used for the checkmark when checked disabledCheckedColor: Color color that will be used for the box and border when disabled and checked disabledUncheckedColor: Color color that will be used for the border when disabled and unchecked. By default, the inner box is transparent when unchecked. disabledIndeterminateColor: Color color that will be used for the box and border in an ToggleableState.Indeterminate state Returns [CheckboxColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_checkboxcolors) |