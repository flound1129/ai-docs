# SecondaryButton Function

*Modifiers:
final*

Use a secondary button for medium-emphasis action on a surface. Examples of when to use a secondary button might include:

- Inverse actions: The inverse of the primary action, for example, to Remove a friend request. - Continuation actions: Actions like See More. - Supporting actions: Actions that support a primary action.

## Signature

```kotlin
fun SecondaryButton(label: String, onClick: () -> Unit, modifier: Modifier, leading: () -> Unit? = null, isEnabled: Boolean = true, expanded: Boolean = false, colors: SecondaryButtonColors = SecondaryButtonDefaults.colors(), labelTextStyle: TextStyle?, contentAlignment: Alignment.Horizontal)
```

## Parameters

label:
String
The text to display on the button.
onClick:
Function0
The callback to invoke when the button is clicked.
modifier:
Modifier
Modifier to be applied to the button.
leading:
Function0?
An optional composable to display as a leading icon.
isEnabled:
Boolean
Whether the button is enabled or not.
expanded:
Boolean
Whether the button should be expanded or not.
colors:
[SecondaryButtonColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_button_foundation_secondarybuttoncolors)
The colors to use for different states of the button.
labelTextStyle:
TextStyle?
The text style to be used for the label.
contentAlignment:
Alignment.Horizontal
The horizontal alignment of the icon and label.