# GrabbableSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

GrabbableSystem is a System that allows for grabbing of objects in the scene. It is responsible for detecting when an object is grabbed and then updating the object's position and rotation to match the grabber's position and rotation. It also handles the release of the object when the grabber releases it.

This System comes default with Meta Spatial SDK and operates on entities with [Grabbable](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_grabbable) components. It interacts with [Controller](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_controller) components to detect grab inputs and can affect [Followable](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_followable) components by disabling them during grabs.

## Signature

```kotlin
class GrabbableSystem : SystemBase
```

## Constructors

| **GrabbableSystem** () | Signature ```kotlin constructor() ``` Returns [GrabbableSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_grabbablesystem) |
| --- | --- |

## Properties

| **active** : Boolean [Get][Set] | Signature ```kotlin var active: Boolean ``` |
| --- | --- |
| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| **grabButtons** : Int [Get][Set] | The default is just grabbing with the grip buttons. You can change the grab buttons by accessing the grabButtons variable of the GrabbableSystem: Example: ```kotlin systemManager.findSystem<GrabbableSystem>().grabButtons = (ButtonBits.ButtonSqueezeR or ButtonBits.ButtonSqueezeL or ButtonBits.ButtonX) ``` Signature ```kotlin var grabButtons: Int ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **delete** ( entity ) | System should do any housekeeping based on [GrabbableSystem.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_grabbablesystem#delete) being removed from the scene Signature ```kotlin open override fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |