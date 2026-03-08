# BorderedIconButton Function

*Modifiers:
final*

A bordered icon button is a medium-emphasis button with only an icon, a transparent background, and a thin border. Use for actions that need more emphasis than a borderless icon button.

## Signature

```kotlin
fun BorderedIconButton(icon: () -> Unit, onClick: () -> Unit, modifier: Modifier, colors: BorderedButtonColors = BorderedButtonDefaults.colors(), borderColor: Color?, isEnabled: Boolean = true, expanded: Boolean = false)
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
[BorderedButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_button_foundation_borderedbuttoncolors)
The colors to use for different states of the button.
borderColor:
Color?
The color of the border. If null, uses the default bordered border color.
isEnabled:
Boolean
Whether the button is enabled or not. Defaults to true.
expanded:
Boolean
Whether the button should be expanded or not. Defaults to false.