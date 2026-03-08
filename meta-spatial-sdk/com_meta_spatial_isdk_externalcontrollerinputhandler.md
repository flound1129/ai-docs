# ExternalControllerInputHandler Interface

Interface used to integrate ISDK with other systems that may be using the controllers. Can be used to disable ISDK input handling if the controllers are in use by another system.

## Signature

```kotlin
interface ExternalControllerInputHandler
```

## Functions

| **areControllersInUse** () | Used by ISDK to check if the controllers are currently in use by an external system (e.g., locomotion). Signature ```kotlin abstract fun areControllersInUse(): Boolean ``` Returns Boolean true if any controllers are in use by an external system and thus input should be ignored by ISDK. |
| --- | --- |
| **setControllerInputResult** ( entity , result ) | Notifies the handler about the input usage result for a specific controller entity. Signature ```kotlin abstract fun setControllerInputResult(entity: Entity, result: Boolean) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The controller entity whose input usage state is being set. result: Boolean true if the controller is in use by ISDK, false otherwise. |