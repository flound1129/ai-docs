# ButtonClickEventArgs Class

Extends
[EventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_eventargs)
*Modifiers:
final*

Event arguments for button click events.

ButtonClickEventArgs is used to pass information about a button click interaction through the event system. It contains a [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) object that provides details about the interaction, such as the hit point, normal, and distance.

This class is typically used when registering event listeners for button click events on entities, allowing components to respond to user interactions.

Example usage:

```kotlin // Register a button click event listener on an entity
entity.registerEventListener<ButtonClickEventArgs>(ButtonClickEventArgs.EVENT_NAME) { entity, eventArgs ->
    // Handle the button click event
    val hitPoint = eventArgs.hitInfo.hitPoint
    // Perform actions based on the click
}
// Send a button click event to an entity
dataModel.sendEvent(
    entity,
    ButtonClickEventArgs.EVENT_NAME,
    ButtonClickEventArgs.fromHitInfo(hitInfo, dataModel)
) ```

## Signature

```kotlin
class ButtonClickEventArgs(val hitInfo: HitInfo, val dataModel: DataModel) : EventArgs
```

## Constructors

| **ButtonClickEventArgs** ( hitInfo , dataModel ) | Signature ```kotlin constructor(hitInfo: HitInfo, dataModel: DataModel) ``` Parameters hitInfo: [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) Information about the hit/interaction that triggered the button click dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The data model associated with this event Returns [ButtonClickEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttonclickeventargs) |
| --- | --- |

## Properties

| **dataModel** : [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) [Get] | Signature ```kotlin val dataModel: DataModel ``` |
| --- | --- |
| **eventName** : String [Get] | Signature ```kotlin val eventName: String ``` |
| **handled** : Boolean [Get][Set] | Signature ```kotlin var handled: Boolean ``` |
| **hitInfo** : [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) [Get] | Information about the hit/interaction that triggered the button click Signature ```kotlin val hitInfo: HitInfo ``` |
| **throttleTime** : Int? [Get][Set] | Signature ```kotlin var throttleTime: Int? ``` |

## Companion Object

### Companion Object Properties

| **EVENT_NAME** : String [Get] | The name of the button click event, used when registering event listeners. Signature ```kotlin const val EVENT_NAME: String ``` |
| --- | --- |

### Companion Object Functions

| **fromHitInfo** ( hitInfo , dataModel ) | Creates a ButtonClickEventArgs instance from a HitInfo object and DataModel. This factory method provides a convenient way to create ButtonClickEventArgs instances when sending events. Signature ```kotlin fun fromHitInfo(hitInfo: HitInfo, dataModel: DataModel): ButtonClickEventArgs ``` Parameters hitInfo: [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) Information about the hit/interaction that triggered the button click dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The data model associated with this event Returns [ButtonClickEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttonclickeventargs) A new ButtonClickEventArgs instance |
| --- | --- |