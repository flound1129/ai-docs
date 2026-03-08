# ButtonHoverMoveEventArgs Class

Extends
[EventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_eventargs)
*Modifiers:
final*

Event arguments for hover movement events.

ButtonHoverMoveEventArgs is used to pass information about hover movement interactions through the event system. It contains a [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) object that provides details about the interaction, such as the hit point, normal, and distance.

This class is typically used when registering event listeners for hover movement events on entities, allowing components to respond to continuous hover movements over an object.

Example usage:

```kotlin // Register a hover movement event listener on an entity
entity.registerEventListener<ButtonHoverMoveEventArgs>(ButtonHoverMoveEventArgs.EVENT_NAME) { entity, eventArgs ->
    // Handle the hover movement event
    val hitPoint = eventArgs.hitInfo.hitPoint
    // Update UI elements based on hover position
    updateCursorPosition(hitPoint)
    // Or perform other hover-related interactions
    updateHoverFeedback(eventArgs.hitInfo)
} ```

## Signature

```kotlin
class ButtonHoverMoveEventArgs(val hitInfo: HitInfo, val dataModel: DataModel) : EventArgs
```

## Constructors

| **ButtonHoverMoveEventArgs** ( hitInfo , dataModel ) | Signature ```kotlin constructor(hitInfo: HitInfo, dataModel: DataModel) ``` Parameters hitInfo: [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) Information about the hit/interaction during the hover movement dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The data model associated with this event Returns [ButtonHoverMoveEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttonhovermoveeventargs) |
| --- | --- |

## Properties

| **dataModel** : [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) [Get] | Signature ```kotlin val dataModel: DataModel ``` |
| --- | --- |
| **eventName** : String [Get] | Signature ```kotlin val eventName: String ``` |
| **handled** : Boolean [Get][Set] | Signature ```kotlin var handled: Boolean ``` |
| **hitInfo** : [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) [Get] | Information about the hit/interaction during the hover movement Signature ```kotlin val hitInfo: HitInfo ``` |
| **throttleTime** : Int? [Get][Set] | Signature ```kotlin var throttleTime: Int? ``` |

## Companion Object

### Companion Object Properties

| **EVENT_NAME** : String [Get] | The name of the hover movement event, used when registering event listeners. Signature ```kotlin const val EVENT_NAME: String ``` |
| --- | --- |

### Companion Object Functions

| **fromHitInfo** ( hitInfo , dataModel ) | Creates a ButtonHoverMoveEventArgs instance from a HitInfo object and DataModel. This factory method provides a convenient way to create ButtonHoverMoveEventArgs instances when sending events. Signature ```kotlin fun fromHitInfo(hitInfo: HitInfo, dataModel: DataModel): ButtonHoverMoveEventArgs ``` Parameters hitInfo: [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) Information about the hit/interaction during the hover movement dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The data model associated with this event Returns [ButtonHoverMoveEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttonhovermoveeventargs) A new ButtonHoverMoveEventArgs instance |
| --- | --- |