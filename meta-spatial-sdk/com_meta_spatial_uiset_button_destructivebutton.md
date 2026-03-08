# DestructiveButton Function

*Modifiers:
final*

Used to draw the user's attention to a destructive action such as "Delete Account" or "End the Call". The red color is meant to give users pause before they take the action.

## Signature

```kotlin
fun DestructiveButton(label: String, onClick: () -> Unit, leading: () -> Unit? = null, isEnabled: Boolean = true, expanded: Boolean = false)
```

## Parameters

label:
String
The text to display on the button.
onClick:
Function0
The callback to invoke when the button is clicked.
leading:
Function0?
An optional icon to display before the label.
isEnabled:
Boolean
Whether the button is enabled or disabled.
expanded:
Boolean
Whether the button should be expanded to fill its container.