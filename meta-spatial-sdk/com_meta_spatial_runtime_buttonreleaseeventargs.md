# ButtonReleaseEventArgs Class

Extends
[EventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_eventargs)
*Modifiers:
final*

Event arguments for button release events.

ButtonReleaseEventArgs is used to pass information about a button release interaction through the event system. It contains a [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) object that provides details about the interaction, such as the hit point, normal, and distance, as well as the specific [ControllerButton](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_controllerbutton) that was released.

This class is typically used when registering event listeners for button release events on entities, allowing components to respond to specific button release inputs.

Example usage:

```kotlin // Register a button release event listener on an entity
entity.registerEventListener<ButtonReleaseEventArgs>(ButtonReleaseEventArgs.EVENT_NAME) { entity, eventArgs ->
    // Handle the button release event
    val hitPoint = eventArgs.hitInfo.hitPoint
    val button = eventArgs.button
    // Perform actions based on which button was released
    when (button) {
        ControllerButton.A -> handleAButtonRelease()
        ControllerButton.LeftTrigger -> handleLeftTriggerRelease()
        // Handle other buttons...
    }
} ```

## Signature

```kotlin
class ButtonReleaseEventArgs(val hitInfo: HitInfo, val button: ControllerButton, val dataModel: DataModel) : EventArgs
```

## Constructors

| **ButtonReleaseEventArgs** ( hitInfo , button , dataModel ) | Signature ```kotlin constructor(hitInfo: HitInfo, button: ControllerButton, dataModel: DataModel) ``` Parameters hitInfo: [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) Information about the hit/interaction that triggered the button release button: [ControllerButton](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_controllerbutton) The specific controller button that was released dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The data model associated with this event Returns [ButtonReleaseEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttonreleaseeventargs) |
| --- | --- |

## Properties

| **button** : [ControllerButton](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_controllerbutton) [Get] | The specific controller button that was released Signature ```kotlin val button: ControllerButton ``` |
| --- | --- |
| **dataModel** : [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) [Get] | Signature ```kotlin val dataModel: DataModel ``` |
| **eventName** : String [Get] | Signature ```kotlin val eventName: String ``` |
| **handled** : Boolean [Get][Set] | Signature ```kotlin var handled: Boolean ``` |
| **hitInfo** : [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) [Get] | Information about the hit/interaction that triggered the button release Signature ```kotlin val hitInfo: HitInfo ``` |
| **throttleTime** : Int? [Get][Set] | Signature ```kotlin var throttleTime: Int? ``` |

## Companion Object

### Companion Object Properties

| **EVENT_NAME** : String [Get] | The name of the button release event, used when registering event listeners. Signature ```kotlin const val EVENT_NAME: String ``` |
| --- | --- |

### Companion Object Functions

| **fromHitInfo** ( hitInfo , dataModel , changed ) | Creates a ButtonReleaseEventArgs instance from a HitInfo object, DataModel, and button identifier. This factory method provides a convenient way to create ButtonReleaseEventArgs instances when sending events. It maps the raw button identifier (from ButtonBits) to the corresponding ControllerButton enum value. Signature ```kotlin fun fromHitInfo(hitInfo: HitInfo, dataModel: DataModel, changed: Int): ButtonReleaseEventArgs ``` Parameters hitInfo: [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) Information about the hit/interaction that triggered the button release dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The data model associated with this event changed: Int The raw button identifier (from ButtonBits) that was released Returns [ButtonReleaseEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttonreleaseeventargs) A new ButtonReleaseEventArgs instance |
| --- | --- |