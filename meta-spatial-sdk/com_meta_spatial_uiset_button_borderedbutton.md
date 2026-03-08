# BorderedButton Function

*Modifiers:
final*

A bordered button is a medium-emphasis button. It has a transparent background and a thin border, making it suitable for secondary actions that need more emphasis than a borderless button but less than a primary button.

## Signature

```kotlin
fun BorderedButton(label: String, onClick: () -> Unit, modifier: Modifier, leading: () -> Unit? = null, isEnabled: Boolean = true, expanded: Boolean = false, colors: BorderedButtonColors = BorderedButtonDefaults.colors(), borderColor: Color?, labelTextStyle: TextStyle?, contentAlignment: Alignment.Horizontal)
```

## Parameters

label:
String
The text to display on the button.
onClick:
Function0
The callback to be invoked when the button is clicked.
modifier:
Modifier
Modifier to be applied to the button.
leading:
Function0?
An optional icon to display before the label.
isEnabled:
Boolean
Whether the button is enabled or not. Defaults to true.
expanded:
Boolean
Whether the button should be expanded or not. Defaults to false.
colors:
[BorderedButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_button_foundation_borderedbuttoncolors)
The colors to use for different states of the button.
borderColor:
Color?
The color of the border. If null, uses the default bordered border color.
labelTextStyle:
TextStyle?
The text style to be used for the label.
contentAlignment:
Alignment.Horizontal
The horizontal alignment of the icon and label. Defaults to Alignment.CenterHorizontally.