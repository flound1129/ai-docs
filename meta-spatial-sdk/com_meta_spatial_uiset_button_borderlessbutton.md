# BorderlessButton Function

*Modifiers:
final*

A borderless button doesn't have a background. Use it for less-frequent actions to maintain emphasis on other actions.

## Signature

```kotlin
fun BorderlessButton(label: String, onClick: () -> Unit, leading: () -> Unit? = null, isEnabled: Boolean = true, expanded: Boolean = false)
```

## Parameters

label:
String
The text to display on the button.
onClick:
Function0
The action to perform when the button is clicked.
leading:
Function0?
An optional icon to display before the label.
isEnabled:
Boolean
Whether the button is enabled or disabled.
expanded:
Boolean
Whether the button should be expanded to fill its parent.