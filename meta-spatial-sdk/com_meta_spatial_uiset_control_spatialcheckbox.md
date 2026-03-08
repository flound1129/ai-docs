# SpatialCheckbox Function

*Modifiers:
final*

Checkboxes allow users to select one or more items from a set. Checkboxes can turn an option on or off.

## Signature

```kotlin
fun SpatialCheckbox(checked: Boolean, onCheckedChange: (Boolean) -> Unit?, modifier: Modifier, enabled: Boolean = true)
```

## Parameters

checked:
Boolean
whether this checkbox is checked or unchecked
onCheckedChange:
Function1?
called when this checkbox is clicked. If
`null`
, then this checkbox will not be interactable, unless something else handles its input events and updates its state.
modifier:
Modifier
the Modifier to be applied to this checkbox
enabled:
Boolean
controls the enabled state of this checkbox. When
`false`
, this component will not respond to user input, and it will appear visually disabled and disabled to accessibility services.