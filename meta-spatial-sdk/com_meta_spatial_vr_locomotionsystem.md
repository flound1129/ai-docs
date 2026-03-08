# LocomotionSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

## Signature

```kotlin
class LocomotionSystem(val locomotionControls: LocomotionControls = LocomotionControls.Right, val canCallbacksConsumeLeftRightInput: Boolean = true) : SystemBase
```

## Constructors

| **LocomotionSystem** ( locomotionControls , canCallbacksConsumeLeftRightInput ) | Signature ```kotlin constructor(locomotionControls: LocomotionControls = LocomotionControls.Right, canCallbacksConsumeLeftRightInput: Boolean = true) ``` Parameters locomotionControls: [LocomotionControls](/reference/spatial-sdk/v0.10.1/com_meta_spatial_vr_locomotioncontrols) canCallbacksConsumeLeftRightInput: Boolean Returns [LocomotionSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_vr_locomotionsystem) |
| --- | --- |

## Properties

| **canCallbacksConsumeLeftRightInput** : Boolean [Get] | Signature ```kotlin val canCallbacksConsumeLeftRightInput: Boolean = true ``` |
| --- | --- |
| **cursor** : [SceneObject?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneobject) [Get][Set] | Signature ```kotlin var cursor: SceneObject? ``` |
| **cursorMesh** : [SceneMesh?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenemesh) [Get][Set] | Signature ```kotlin var cursorMesh: SceneMesh? ``` |
| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| **locomoteState** : [LocomoteState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_vr_locomotestate) [Get][Set] | Signature ```kotlin var locomoteState: LocomoteState ``` |
| **locomotionControls** : [LocomotionControls](/reference/spatial-sdk/v0.10.1/com_meta_spatial_vr_locomotioncontrols) [Get] | Signature ```kotlin val locomotionControls: LocomotionControls ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |
| **warpSound** : Lazy<SceneAudioAsset> [Get] | Signature ```kotlin val warpSound: Lazy<SceneAudioAsset> ``` |

## Functions

| **areControllersInUse** () | Signature ```kotlin fun areControllersInUse(): Boolean ``` Returns Boolean |
| --- | --- |
| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| **delete** ( entity ) | System should do any housekeeping based on [SystemBase.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase#delete) being removed from the scene Signature ```kotlin open fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open fun destroy() ``` |
| **enableLocomotion** ( enabled ) | Signature ```kotlin fun enableLocomotion(enabled: Boolean) ``` Parameters enabled: Boolean |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getControllerInputResult** ( entity ) | Signature ```kotlin fun getControllerInputResult(entity: Entity): Boolean ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) Returns Boolean |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open override fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **setControllerInputResult** ( entity , value ) | Signature ```kotlin fun setControllerInputResult(entity: Entity, value: Boolean) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) value: Boolean |