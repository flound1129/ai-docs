# SpatialRadioButton Function

*Modifiers:
final*

Radio buttons allow users to select one option from a set.

## Signature

```kotlin
fun SpatialRadioButton(selected: Boolean, onClick: () -> Unit?, modifier: Modifier, enabled: Boolean = true)
```

## Parameters

selected:
Boolean
whether this radio button is selected or not
onClick:
Function0?
called when this radio button is clicked. If
`null`
, then this radio button will not be interactable, unless something else handles its input events and updates its state.
modifier:
Modifier
the Modifier to be applied to this radio button
enabled:
Boolean
controls the enabled state of this radio button. When
`false`
, this component will not respond to user input, and it will appear visually disabled and disabled to accessibility services.