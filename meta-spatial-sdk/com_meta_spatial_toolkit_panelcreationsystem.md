# PanelCreationSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

PanelCreationSystem is responsible for creating [PanelSceneObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelsceneobject) s for Entities with the [Panel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panel) component. The PanelCreationSystem takes the registrations from [AppSystemActivity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_appsystemactivity) .registerPanels(), uses the PanelConfigOptions to create [PanelSceneObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelsceneobject) s, and then links them with the [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) .

This System comes default with Meta Spatial SDK and operates on entities with [Panel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panel) components.

## Signature

```kotlin
class PanelCreationSystem(val panelCreator: HashMap<Int, (ent: Entity) -> PanelSceneObject>) : SystemBase
```

## Constructors

| **PanelCreationSystem** ( panelCreator ) | Signature ```kotlin constructor(panelCreator: HashMap<Int, (ent: Entity) -> PanelSceneObject>) ``` Parameters panelCreator: HashMap A map of panel registration IDs to functions that create panels. Returns [PanelCreationSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelcreationsystem) |
| --- | --- |

## Properties

| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| --- | --- |
| **panelCreator** : HashMap [Get] | A map of panel registration IDs to functions that create panels. Signature ```kotlin val panelCreator: HashMap<Int, (ent: Entity) -> PanelSceneObject> ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **delete** ( ent ) | System should do any housekeeping based on entity being removed from the scene Signature ```kotlin open override fun delete(ent: Entity) ``` Parameters ent: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open override fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **forEachPanel** ( action ) | Iterate over all panels. Signature ```kotlin fun forEachPanel(action: (Entity, CompletableFuture<PanelSceneObject>) -> Unit) ``` Parameters action: Function2 |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |