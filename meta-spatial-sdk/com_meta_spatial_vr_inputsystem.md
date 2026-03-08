# InputSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

## Constructors

| **InputSystem** ( locomotionSystem , ctx ) | Signature ```kotlin constructor(locomotionSystem: LocomotionSystem, ctx: Context) ``` Parameters locomotionSystem: [LocomotionSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_vr_locomotionsystem) ctx: Context Returns [InputSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_vr_inputsystem) |
| --- | --- |

## Properties

| **active** : Boolean [Get] | Signature ```kotlin var active: Boolean ``` |
| --- | --- |
| **ctx** : Context [Get] | Signature ```kotlin val ctx: Context ``` |
| **cursorActuatedRatio** : Float [Get][Set] | Signature ```kotlin var cursorActuatedRatio: Float ``` |
| **cursorDepthScale** : Float [Get][Set] | Signature ```kotlin var cursorDepthScale: Float ``` |
| **cursorScale** : Float [Get][Set] | Signature ```kotlin var cursorScale: Float ``` |
| **cursorScaleMultiplier** : Float [Get][Set] | Signature ```kotlin var cursorScaleMultiplier: Float ``` |
| **directInputEnabled** : Boolean [Get] | Signature ```kotlin var directInputEnabled: Boolean ``` |
| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| **locomotionSystem** : [LocomotionSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_vr_locomotionsystem) [Get] | Signature ```kotlin val locomotionSystem: LocomotionSystem ``` |
| **maxPointerDistance** : Float [Get][Set] | Signature ```kotlin var maxPointerDistance: Float ``` |
| **preBuiltQuery** : BuiltQuery [Get] | Signature ```kotlin val preBuiltQuery: BuiltQuery ``` |
| **selectButtons** : Int [Get][Set] | Signature ```kotlin var selectButtons: Int ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |
| **touchButtons** : Int [Get][Set] | Signature ```kotlin var touchButtons: Int ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **delete** ( entity ) | System should do any housekeeping based on [SystemBase.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase#delete) being removed from the scene Signature ```kotlin open fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open override fun destroy() ``` |
| **enableDirectInput** ( enabled ) | Signature ```kotlin fun enableDirectInput(enabled: Boolean) ``` Parameters enabled: Boolean |
| **enableInput** ( enabled ) | Signature ```kotlin fun enableInput(enabled: Boolean) ``` Parameters enabled: Boolean |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **setLeftHandDirectionOverride** ( lookDirection ) | Overrides the natural direction of the left hand controller with a custom look direction. When set, the controller's pose rotation will be calculated using this direction instead of the controller's natural orientation. Signature ```kotlin fun setLeftHandDirectionOverride(lookDirection: Vector3?) ``` Parameters lookDirection: [Vector3?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The direction vector to override the left hand controller's look direction, or null to disable the override and use natural controller orientation. Example: ```kotlin // Point left hand controller towards a specific target val targetDirection = Vector3(1.0f, 0.0f, 0.0f) // Point right inputSystem.setLeftHandDirectionOverride(targetDirection) // Restore natural controller orientation inputSystem.setLeftHandDirectionOverride(null) ``` |
| **setRightHandDirectionOverride** ( lookDirection ) | Overrides the natural direction of the right hand controller with a custom look direction. When set, the controller's pose rotation will be calculated using this direction instead of the controller's natural orientation. Signature ```kotlin fun setRightHandDirectionOverride(lookDirection: Vector3?) ``` Parameters lookDirection: [Vector3?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The direction vector to override the right hand controller's look direction, or null to disable the override and use natural controller orientation. Example: ```kotlin // Point right hand controller towards a specific target val targetDirection = Vector3(-1.0f, 0.0f, 0.0f) // Point left inputSystem.setRightHandDirectionOverride(targetDirection) // Restore natural controller orientation inputSystem.setRightHandDirectionOverride(null) ``` |

## Companion Object

### Companion Object Properties

| **DEFAULT_CURSOR_ACTUATED_RATIO** : Float [Get] | Signature ```kotlin val DEFAULT_CURSOR_ACTUATED_RATIO: Float ``` |
| --- | --- |
| **DEFAULT_CURSOR_DEPTH_SCALE** : Float [Get] | Signature ```kotlin val DEFAULT_CURSOR_DEPTH_SCALE: Float = 0.0112f ``` |
| **DEFAULT_CURSOR_SCALE** : Float [Get] | Signature ```kotlin val DEFAULT_CURSOR_SCALE: Float = 3.2E-4f ``` |
| **DEFAULT_CURSOR_SCALE_MULTIPLIER** : Float [Get] | Signature ```kotlin val DEFAULT_CURSOR_SCALE_MULTIPLIER: Float = 0.75f ``` |