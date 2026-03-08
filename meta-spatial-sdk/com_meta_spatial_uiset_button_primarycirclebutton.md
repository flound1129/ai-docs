# PrimaryCircleButton Function

*Modifiers:
final*

A primary circular button without text label.

## Signature

```kotlin
fun PrimaryCircleButton(icon: () -> Unit, onClick: () -> Unit, modifier: Modifier, colors: PrimaryButtonColors = PrimaryButtonDefaults.colors(), isEnabled: Boolean = true)
```

## Parameters

icon:
Function0
The icon to display on the button.
onClick:
Function0
The callback to be invoked when the button is clicked.
modifier:
Modifier
Modifier to be applied to the button.
colors:
[PrimaryButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_button_foundation_primarybuttoncolors)
The colors to use for different states of the button.
isEnabled:
Boolean
Whether the button is enabled or not. Defaults to true.