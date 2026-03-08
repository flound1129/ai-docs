# ButtonHoverEventArgs Class

Extends
[EventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_eventargs)
*Modifiers:
final*

Event arguments for hover events.

ButtonHoverEventArgs is used to pass information about hover interactions through the event system. It indicates whether a hover interaction is starting or ending via the [ButtonHoverEventArgs.isStart](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttonhovereventargs#isstart) property.

This class is typically used when registering event listeners for hover events on entities, allowing components to respond when a controller begins or ends hovering over an object.

Example usage:

```kotlin // Register a hover event listener on an entity
entity.registerEventListener<ButtonHoverEventArgs>(ButtonHoverEventArgs.EVENT_NAME) { entity, eventArgs ->
    // Handle the hover event
    if (eventArgs.isStart) {
        // Controller has started hovering over this entity
    } else {
        // Controller has stopped hovering over this entity
    }
} ```

## Signature

```kotlin
class ButtonHoverEventArgs(val isStart: Boolean, val dataModel: DataModel) : EventArgs
```

## Constructors

| **ButtonHoverEventArgs** ( isStart , dataModel ) | Signature ```kotlin constructor(isStart: Boolean, dataModel: DataModel) ``` Parameters isStart: Boolean True if the hover is starting, false if it's ending dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The data model associated with this event Returns [ButtonHoverEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttonhovereventargs) |
| --- | --- |

## Properties

| **dataModel** : [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) [Get] | Signature ```kotlin val dataModel: DataModel ``` |
| --- | --- |
| **eventName** : String [Get] | Signature ```kotlin val eventName: String ``` |
| **handled** : Boolean [Get][Set] | Signature ```kotlin var handled: Boolean ``` |
| **isStart** : Boolean [Get] | True if the hover is starting, false if it's ending Signature ```kotlin val isStart: Boolean ``` |
| **throttleTime** : Int? [Get][Set] | Signature ```kotlin var throttleTime: Int? ``` |

## Companion Object

### Companion Object Properties

| **EVENT_NAME** : String [Get] | The name of the hover event, used when registering event listeners. Signature ```kotlin const val EVENT_NAME: String ``` |
| --- | --- |

### Companion Object Functions

| **fromHitInfo** ( isStart , dataModel ) | Creates a ButtonHoverEventArgs instance. This factory method provides a convenient way to create ButtonHoverEventArgs instances when sending events. Signature ```kotlin fun fromHitInfo(isStart: Boolean, dataModel: DataModel): ButtonHoverEventArgs ``` Parameters isStart: Boolean True if the hover is starting, false if it's ending dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The data model associated with this event Returns [ButtonHoverEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttonhovereventargs) A new ButtonHoverEventArgs instance |
| --- | --- |