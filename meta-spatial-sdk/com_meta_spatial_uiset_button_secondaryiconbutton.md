# SecondaryIconButton Function

*Modifiers:
final*

A secondary icon button without text label.

## Signature

```kotlin
fun SecondaryIconButton(icon: () -> Unit, onClick: () -> Unit, modifier: Modifier, colors: SecondaryButtonColors = SecondaryButtonDefaults.colors(), isEnabled: Boolean = true)
```

## Parameters

icon:
Function0
The icon to display on the button.
onClick:
Function0
The action to perform when the button is clicked.
modifier:
Modifier
Modifier to be applied to the button.
colors:
[SecondaryButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_button_foundation_secondarybuttoncolors)
The colors to use for different states of the button.
isEnabled:
Boolean
Whether the button is enabled or disabled.