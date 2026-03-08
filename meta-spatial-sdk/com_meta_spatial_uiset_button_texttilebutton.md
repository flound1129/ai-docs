# TextTileButton Function

*Modifiers:
final*

Text tile buttons have stacked layout, and can contain a button and a secondary text as optional elements. They have an active state when toggled on.

## Signature

```kotlin
fun TextTileButton(label: String, onSelectionChange: (Boolean) -> Unit, modifier: Modifier, secondaryLabel: String? = null, enabled: Boolean = true, selected: Boolean = false, icon: () -> Unit? = null)
```

## Parameters

label:
String
The text label to be displayed in the button.
onSelectionChange:
Function1
The callback to be invoked when the button is clicked.
modifier:
Modifier
The Modifier to be applied to this button.
secondaryLabel:
String?
The secondary text label to be displayed in the button.
enabled:
Boolean
Whether this button is enabled or not.
selected:
Boolean
Whether this button is selected or not.
icon:
Function0?
The icon to be displayed in the button.