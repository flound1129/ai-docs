# ButtonShelf Function

*Modifiers:
final*

Button shelves have a stacked layout. They have an active state when toggled on.

## Signature

```kotlin
fun ButtonShelf(modifier: Modifier, icon: () -> Unit, label: String, enabled: Boolean = true, selected: Boolean = false, onSelectionChange: (Boolean) -> Unit)
```

## Parameters

modifier:
Modifier
The Modifier to be applied to this button.
icon:
Function0
The icon to be displayed in the button.
label:
String
The text label to be displayed in the button.
enabled:
Boolean
Whether this button is enabled or not.
selected:
Boolean
Whether this button is selected or not.
onSelectionChange:
Function1
The callback to be invoked when the button is clicked.