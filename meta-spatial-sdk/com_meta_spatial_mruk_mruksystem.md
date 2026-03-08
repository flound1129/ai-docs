# MRUKSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

System responsible for managing Mixed Reality Utility Kit (MRUK) operations within the spatial scene.

The MRUKSystem handles core MRUK functionality including scene ticking and entity cleanup for MRUK-related components. It extends SystemBase and integrates with the spatial SDK system architecture to provide seamless mixed reality scene management.

Key responsibilities:

- Ticks the MR scene and global context on each execution cycle - Cleans up entity-to-material mappings when entities are deleted - Maintains synchronization between the spatial scene and MRUK native layer

## Signature

```kotlin
class MRUKSystem : SystemBase
```

## Constructors

| **MRUKSystem** () | Signature ```kotlin constructor() ``` Returns [MRUKSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mruksystem) |
| --- | --- |

## Properties

| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| --- | --- |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **delete** ( entity ) | Handles cleanup when an entity is deleted from the scene. Removes any associated scene material mappings for the deleted entity from the [AnchorProceduralMesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_anchorproceduralmesh) cache to prevent memory leaks and stale references. Signature ```kotlin open override fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity being deleted from the scene. |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | Executes the MRUK system update cycle. This method is called each frame to tick the MR scene and update the global MRUK context, ensuring synchronization between the spatial scene and the native MRUK layer. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |