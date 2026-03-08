# VisibleSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

This System uses the Visible component to show/hide entity meshes.

This System comes default with Meta Spatial SDK and operates on entities with [Visible](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_visible) component. It updates the visibility of [SceneObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneobject) commonly added via [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) or [Panel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panel) components.

It depends on [SceneObjectSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_sceneobjectsystem) to access the SceneObjects associated with entities and must run after [MeshCreationSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_meshcreationsystem) to ensure visibility is set correctly when meshes are created.

## Signature

```kotlin
class VisibleSystem : SystemBase
```

## Constructors

| **VisibleSystem** () | Signature ```kotlin constructor() ``` Returns [VisibleSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_visiblesystem) |
| --- | --- |

## Properties

| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| --- | --- |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **delete** ( entity ) | System should do any housekeeping based on [SystemBase.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase#delete) being removed from the scene Signature ```kotlin open fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | This system must run after the MeshCreationSystem. Signature ```kotlin open override fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |