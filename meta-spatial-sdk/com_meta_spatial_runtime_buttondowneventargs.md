# ButtonDownEventArgs Class

Extends
[EventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_eventargs)
*Modifiers:
final*

Event arguments for button press events.

ButtonDownEventArgs is used to pass information about a button press interaction through the event system. It contains a [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) object that provides details about the interaction, such as the hit point, normal, and distance, as well as the specific [ControllerButton](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_controllerbutton) that was pressed.

This class is typically used when registering event listeners for button press events on entities, allowing components to respond to specific button inputs.

Example usage:

```kotlin // Register a button press event listener on an entity
entity.registerEventListener<ButtonDownEventArgs>(ButtonDownEventArgs.EVENT_NAME) { entity, eventArgs ->
    // Handle the button press event
    val hitPoint = eventArgs.hitInfo.hitPoint
    val button = eventArgs.button
    // Perform actions based on which button was pressed
    when (button) {
        ControllerButton.A -> handleAButtonPress()
        ControllerButton.LeftTrigger -> handleLeftTriggerPress()
        // Handle other buttons...
    }
} ```

## Signature

```kotlin
class ButtonDownEventArgs(val hitInfo: HitInfo, val button: ControllerButton, val dataModel: DataModel) : EventArgs
```

## Constructors

| **ButtonDownEventArgs** ( hitInfo , button , dataModel ) | Signature ```kotlin constructor(hitInfo: HitInfo, button: ControllerButton, dataModel: DataModel) ``` Parameters hitInfo: [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) Information about the hit/interaction that triggered the button press button: [ControllerButton](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_controllerbutton) The specific controller button that was pressed dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The data model associated with this event Returns [ButtonDownEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttondowneventargs) |
| --- | --- |

## Properties

| **button** : [ControllerButton](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_controllerbutton) [Get] | The specific controller button that was pressed Signature ```kotlin val button: ControllerButton ``` |
| --- | --- |
| **dataModel** : [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) [Get] | Signature ```kotlin val dataModel: DataModel ``` |
| **eventName** : String [Get] | Signature ```kotlin val eventName: String ``` |
| **handled** : Boolean [Get][Set] | Signature ```kotlin var handled: Boolean ``` |
| **hitInfo** : [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) [Get] | Information about the hit/interaction that triggered the button press Signature ```kotlin val hitInfo: HitInfo ``` |
| **throttleTime** : Int? [Get][Set] | Signature ```kotlin var throttleTime: Int? ``` |

## Companion Object

### Companion Object Properties

| **EVENT_NAME** : String [Get] | The name of the button press event, used when registering event listeners. Signature ```kotlin const val EVENT_NAME: String ``` |
| --- | --- |

### Companion Object Functions

| **fromHitInfo** ( hitInfo , dataModel , changed ) | Creates a ButtonDownEventArgs instance from a HitInfo object, DataModel, and button identifier. This factory method provides a convenient way to create ButtonDownEventArgs instances when sending events. It maps the raw button identifier (from ButtonBits) to the corresponding ControllerButton enum value. Signature ```kotlin fun fromHitInfo(hitInfo: HitInfo, dataModel: DataModel, changed: Int): ButtonDownEventArgs ``` Parameters hitInfo: [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) Information about the hit/interaction that triggered the button press dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The data model associated with this event changed: Int The raw button identifier (from ButtonBits) that was pressed Returns [ButtonDownEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttondowneventargs) A new ButtonDownEventArgs instance |
| --- | --- |