# PrimaryButton Function

*Modifiers:
final*

Used to convey the most common, recommended action, such as Done or Complete. People trust the primary button in Meta Horizon OS to be the most obvious, usually preferred choice when progressing through any intent.

## Signature

```kotlin
fun PrimaryButton(label: String, onClick: () -> Unit, modifier: Modifier, leading: () -> Unit? = null, isEnabled: Boolean = true, expanded: Boolean = false, colors: PrimaryButtonColors = PrimaryButtonDefaults.colors(), labelTextStyle: TextStyle?, contentAlignment: Alignment.Horizontal)
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
[PrimaryButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_button_foundation_primarybuttoncolors)
The colors to use for different states of the button.
labelTextStyle:
TextStyle?
The text style to be used for the label.
contentAlignment:
Alignment.Horizontal
The horizontal alignment of the icon and label.