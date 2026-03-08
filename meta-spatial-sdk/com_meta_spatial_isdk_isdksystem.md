# IsdkSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

The IsdkSystem class is responsible for managing and executing the core interaction logic within the ISDK framework. Each frame, it will:

- Updates the Isdk component properties from Spatial SDK toolkit equivalents - Execute interaction logic - Emit pointer events to the scene. - Generate input events from PointerEvents, and emit them to the scene.

It also includes methods to enable debug tools, register for pointer events, and query for additional meta data about PointerEvents.

## Signature

```kotlin
class IsdkSystem(val api: IsdkSystemNativeApi = IsdkSystemNativeApi()) : SystemBase
```

## Constructors

| **IsdkSystem** ( api ) | Signature ```kotlin constructor(api: IsdkSystemNativeApi = IsdkSystemNativeApi()) ``` Parameters api: [IsdkSystemNativeApi](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdksystemnativeapi) The native API that is invoked to execute the core interaction logic. Returns [IsdkSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdksystem) |
| --- | --- |

## Properties

| **api** : [IsdkSystemNativeApi](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdksystemnativeapi) [Get] | The native API that is invoked to execute the core interaction logic. Signature ```kotlin val api: IsdkSystemNativeApi ``` |
| --- | --- |
| **debugToolsEnabled** : Boolean [Get][Set] | Toggles visibility of debug geometry rendering by ISDK, which shows internal state of interactions. Debug visuals have significant performance cost, so this should only be enabled when debugging. Signature ```kotlin var debugToolsEnabled: Boolean ``` |
| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |
| **transformersEnabled** : Boolean [Get][Set] | Enables or disables transformers functionality in ISDK. When enabled, grabbed objects will move according to the behavior defined on the IsdkGrabbable/IsdkGrabConstraint components. When disabled, pointer events will still be emitted; but no transform will take place. Signature ```kotlin var transformersEnabled: Boolean ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **clearInteractableObservers** ( entity ) | Removes all observers for a specific entity, effectively stopping all pointer event notifications for that entity. Signature ```kotlin fun clearInteractableObservers(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity to clear all observers for |
| **delete** ( entity ) | System should do any housekeeping based on [IsdkSystem.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdksystem#delete) being removed from the scene Signature ```kotlin open override fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open override fun destroy() ``` |
| **enableDebugTools** ( enable ) | Signature ```kotlin fun enableDebugTools(enable: Boolean) ``` Parameters enable: Boolean |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open override fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getEventDecoratorId** ( decoratorName ) | Signature ```kotlin fun getEventDecoratorId(decoratorName: String): Long ``` Parameters decoratorName: String Returns Long |
| **getEventDecoratorValueLong** ( pointerEvent , decoratorId ) | Signature ```kotlin fun getEventDecoratorValueLong(pointerEvent: PointerEvent, decoratorId: Long): Long? ``` Parameters pointerEvent: [PointerEvent](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_pointerevent) decoratorId: Long Returns Long? |
| **getHandForPointerEvent** ( pointerEvent ) | Signature ```kotlin fun getHandForPointerEvent(pointerEvent: PointerEvent): Hand? ``` Parameters pointerEvent: [PointerEvent](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_pointerevent) Returns [Hand?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_hand) |
| **getInteractionEventSourceBehavior** ( pointerEvent ) | Signature ```kotlin fun getInteractionEventSourceBehavior(pointerEvent: PointerEvent): InteractionEventSourceBehavior? ``` Parameters pointerEvent: [PointerEvent](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_pointerevent) Returns [InteractionEventSourceBehavior?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_interactioneventsourcebehavior) |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **getScenePointerDistance** () | Gets the current maximum distance for scene pointer interactions in meters. Signature ```kotlin fun getScenePointerDistance(): Float ``` Returns Float The current maximum distance in meters |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **notifyObservers** ( event ) | Signature ```kotlin fun notifyObservers(event: PointerEvent) ``` Parameters event: [PointerEvent](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_pointerevent) |
| **registerExternalControllerInputHandler** ( handler ) | Register an ExternalControllerInputHandler instance, which is used to integrate ISDK with other systems that may be using the controllers. Can be used to disable ISDK input handling if the controllers are in use by another system. Signature ```kotlin fun registerExternalControllerInputHandler(handler: ExternalControllerInputHandler) ``` Parameters handler: [ExternalControllerInputHandler](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_externalcontrollerinputhandler) |
| **registerInteractableObserver** ( entity , observer ) | Registers an observer to receive pointer events for a specific interactable entity. The observer will be called whenever a pointer event occurs on the specified entity. Signature ```kotlin fun registerInteractableObserver(entity: Entity, observer: (PointerEvent) -> Unit): IsdkSystem.InteractableObserverHandle ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity to observe pointer events for observer: Function1 The callback function to invoke when pointer events occur on the entity Returns IsdkSystem.InteractableObserverHandle A handle that can be used to unregister this specific observer |
| **registerObserver** ( observer ) | Signature ```kotlin fun registerObserver(observer: (PointerEvent) -> Unit) ``` Parameters observer: Function1 |
| **setScenePointerDistance** ( distance ) | Sets the maximum distance for scene pointer interactions in meters. This controls how far from scene objects ray-based interactions can detect collisions. Signature ```kotlin fun setScenePointerDistance(distance: Float) ``` Parameters distance: Float The maximum distance in meters (must be positive) |
| **unregisterExternalControllerInputHandler** ( handler ) | Unregister a previously registered ExternalControllerInputHandler instance Signature ```kotlin fun unregisterExternalControllerInputHandler(handler: ExternalControllerInputHandler) ``` Parameters handler: [ExternalControllerInputHandler](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_externalcontrollerinputhandler) |
| **unregisterInteractableObserver** ( handle ) | Unregisters a specific observer using its handle. Signature ```kotlin fun unregisterInteractableObserver(handle: IsdkSystem.InteractableObserverHandle) ``` Parameters handle: IsdkSystem.InteractableObserverHandle The handle returned from registerInteractableObserver |

## Inner Class

### InteractableObserverHandle Class

*Modifiers:
final*

Handle for managing interactable observer registrations

Signature
```kotlin
data class InteractableObserverHandle(val id: Long, val entityId: Long)
```

Constructors
| **InteractableObserverHandle** ( id , entityId ) | Signature ```kotlin constructor(id: Long, entityId: Long) ``` Parameters id: Long entityId: Long Returns IsdkSystem.InteractableObserverHandle |
| --- | --- |

Properties
| **entityId** : Long [Get] | Signature ```kotlin val entityId: Long ``` |
| --- | --- |
| **id** : Long [Get] | Signature ```kotlin val id: Long ``` |