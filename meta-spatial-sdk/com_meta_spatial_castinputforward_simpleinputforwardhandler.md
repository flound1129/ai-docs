# SimpleInputForwardHandler Class

*Modifiers:
final*

An implementation of the InputForwardingHandler interface that passes input events down into [CastInputForwardSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_castinputforward_castinputforwardsystem) .

## Signature

```kotlin
class SimpleInputForwardHandler(val inputForwardSystem: CastInputForwardSystem)
```

## Constructors

| **SimpleInputForwardHandler** ( inputForwardSystem ) | Signature ```kotlin constructor(inputForwardSystem: CastInputForwardSystem) ``` Parameters inputForwardSystem: [CastInputForwardSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_castinputforward_castinputforwardsystem) The [CastInputForwardSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_castinputforward_castinputforwardsystem) that will receive the input events. Returns [SimpleInputForwardHandler](/reference/spatial-sdk/v0.10.1/com_meta_spatial_castinputforward_simpleinputforwardhandler) |
| --- | --- |

## Properties

| **inputForwardSystem** : [CastInputForwardSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_castinputforward_castinputforwardsystem) [Get] | The [CastInputForwardSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_castinputforward_castinputforwardsystem) that will receive the input events. Signature ```kotlin val inputForwardSystem: CastInputForwardSystem ``` |
| --- | --- |
| **keyboardState** : MutableMap [Get] | Signature ```kotlin val keyboardState: MutableMap ``` |

## Functions

| **onClearPressedKeys** () | Signature ```kotlin open fun onClearPressedKeys() ``` |
| --- | --- |
| **onKeyDown** ( keyEvent ) | Signature ```kotlin open fun onKeyDown(keyEvent: KeyEvent) ``` Parameters keyEvent: KeyEvent |
| **onKeyUp** ( keyEvent ) | Signature ```kotlin open fun onKeyUp(keyEvent: KeyEvent) ``` Parameters keyEvent: KeyEvent |
| **onStartInputForwarding** () | Signature ```kotlin open fun onStartInputForwarding() ``` |
| **onStopInputForwarding** () | Signature ```kotlin open fun onStopInputForwarding() ``` |