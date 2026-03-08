# SpatialSwitch Function

*Modifiers:
final*

Switches toggle the state of a single item on or off.

## Signature

```kotlin
fun SpatialSwitch(checked: Boolean, onCheckedChange: (Boolean) -> Unit?, modifier: Modifier, thumbContent: () -> Unit? = null, enabled: Boolean = true, colors: SwitchColors = SwitchDefaults.colors())
```

## Parameters

checked:
Boolean
whether or not this switch is checked
onCheckedChange:
Function1?
called when this switch is clicked. If
`null`
, then this switch will not be interactable, unless something else handles its input events and updates its state.
modifier:
Modifier
the Modifier to be applied to this switch
thumbContent:
Function0?
content that will be drawn inside the thumb, expected to measure
[null.CheckIconSize](/reference/spatial-sdk/v0.10.1/null#checkiconsize)
enabled:
Boolean
controls the enabled state of this switch. When
`false`
, this component will not respond to user input, and it will appear visually disabled and disabled to accessibility services.
colors:
[SwitchColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_switchcolors)
[SwitchColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_switchcolors)
that will be used to resolve the colors used for this switch in different states. See
[SwitchDefaults.colors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_control_switchdefaults#colors)
.