# CastInputForwardSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

CastInputForwardSystem manages the communication between a Spatial SDK app and the MQDH Cast window. Per execute() tick it retrieves the updated mouse/keyboard state info from MQDH Cast and processes the info to manipulate the camera/send input down into the Spatial SDK application.

## Signature

```kotlin
class CastInputForwardSystem(val vrActivity: VrActivity, val initialPose: Pose? = null) : SystemBase
```

## Constructors

| **CastInputForwardSystem** ( vrActivity , initialPose ) | Signature ```kotlin constructor(vrActivity: VrActivity, initialPose: Pose? = null) ``` Parameters vrActivity: [VrActivity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_vractivity) The VrActivity of the Spatial SDK application. initialPose: [Pose?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) Optional pose to initialize the virtual camera with. If null, uses Scene.getViewOrigin(). Returns [CastInputForwardSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_castinputforward_castinputforwardsystem) |
| --- | --- |

## Properties

| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| --- | --- |
| **initialPose** : [Pose?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) [Get] | Optional pose to initialize the virtual camera with. If null, uses Scene.getViewOrigin(). Signature ```kotlin val initialPose: Pose? = null ``` |
| **maxPointerDistance** : Float [Get] | Signature ```kotlin val maxPointerDistance: Float = 5.0f ``` |
| **movementSpeed** : Float [Get][Set] | Signature ```kotlin var movementSpeed: Float ``` |
| **pitchSensitivity** : Float [Get] | Signature ```kotlin val pitchSensitivity: Float = 100.0f ``` |
| **shiftMultiplier** : Float [Get][Set] | Signature ```kotlin var shiftMultiplier: Float ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |
| **vrActivity** : [VrActivity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_vractivity) [Get] | The VrActivity of the Spatial SDK application. Signature ```kotlin val vrActivity: VrActivity ``` |
| **yawSensitivity** : Float [Get] | Signature ```kotlin val yawSensitivity: Float = 100.0f ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **calculateDirectionVector** ( normalizedX , normalizedY , fovLeft , fovRight , fovUp , fovDown ) | Signature ```kotlin fun calculateDirectionVector(normalizedX: Double, normalizedY: Double, fovLeft: Double, fovRight: Double, fovUp: Double, fovDown: Double): Vector3 ``` Parameters normalizedX: Double normalizedY: Double fovLeft: Double fovRight: Double fovUp: Double fovDown: Double Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) |
| **delete** ( entity ) | System should do any housekeeping based on [SystemBase.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase#delete) being removed from the scene Signature ```kotlin open fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open override fun destroy() ``` |
| **destroyPanelAppStreamer** () | Signature ```kotlin fun destroyPanelAppStreamer() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **onPause** () | Signature ```kotlin fun onPause() ``` |
| **onResume** () | Signature ```kotlin fun onResume() ``` |
| **setEnabled** ( enabled ) | Signature ```kotlin fun setEnabled(enabled: Boolean) ``` Parameters enabled: Boolean |