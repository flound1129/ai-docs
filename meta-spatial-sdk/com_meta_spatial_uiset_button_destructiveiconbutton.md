# DestructiveIconButton Function

*Modifiers:
final*

Icon buttons don't have a text label. Icon buttons share the same look and behavior with buttons.

## Signature

```kotlin
fun DestructiveIconButton(icon: () -> Unit, onClick: () -> Unit, isEnabled: Boolean = true)
```

## Parameters

icon:
Function0
The icon to display on the button.
onClick:
Function0
The action to perform when the button is clicked.
isEnabled:
Boolean
Whether the button is enabled or disabled.