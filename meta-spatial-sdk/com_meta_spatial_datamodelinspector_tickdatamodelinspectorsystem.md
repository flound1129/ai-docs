# TickDataModelInspectorSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

## Signature

```kotlin
class TickDataModelInspectorSystem(val spatial: SpatialInterface, val componentManager: ComponentManager) : SystemBase
```

## Constructors

| **TickDataModelInspectorSystem** ( spatial , componentManager ) | Signature ```kotlin constructor(spatial: SpatialInterface, componentManager: ComponentManager) ``` Parameters spatial: [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) componentManager: [ComponentManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentmanager) Returns [TickDataModelInspectorSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_datamodelinspector_tickdatamodelinspectorsystem) |
| --- | --- |

## Properties

| **componentManager** : [ComponentManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentmanager) [Get] | Signature ```kotlin val componentManager: ComponentManager ``` |
| --- | --- |
| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| **spatial** : [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) [Get] | Signature ```kotlin val spatial: SpatialInterface ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **convertMapToJsonString** () | Signature ```kotlin fun convertMapToJsonString(): String ``` Returns String |
| **delete** ( entity ) | System should do any housekeeping based on [SystemBase.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase#delete) being removed from the scene Signature ```kotlin open fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open override fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **toggleEntitySelection** ( entityId ) | Signature ```kotlin fun toggleEntitySelection(entityId: Long) ``` Parameters entityId: Long |