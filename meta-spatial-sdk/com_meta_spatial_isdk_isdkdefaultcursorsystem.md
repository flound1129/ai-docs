# IsdkDefaultCursorSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

System that renders affordances for hovered/selected interactables. When an interaction is active on a mesh surface, this system will render a cursor on at the interaction world location, and a ray towards it from the interactor (hand or controller).

This system subscribes to PointerEvents from the IsdkSystem to determine which cursor visuals should be drawn.

To disable the default cursor visuals, set this system to inactive via the `enableInput` method.

## Constructors

| **IsdkDefaultCursorSystem** ( ctx , isdkSystem ) | Signature ```kotlin constructor(ctx: Context, isdkSystem: IsdkSystem) ``` Parameters ctx: Context isdkSystem: [IsdkSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdksystem) Returns [IsdkDefaultCursorSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdkdefaultcursorsystem) |
| --- | --- |

## Properties

| **active** : Boolean [Get] | Signature ```kotlin var active: Boolean ``` |
| --- | --- |
| **ctx** : Context [Get] | Signature ```kotlin val ctx: Context ``` |
| **cursorConfigActuatedRatio** : Float [Get][Set] | Signature ```kotlin var cursorConfigActuatedRatio: Float ``` |
| **cursorConfigDepthScale** : Float [Get][Set] | Signature ```kotlin var cursorConfigDepthScale: Float ``` |
| **cursorConfigScale** : Float [Get][Set] | Signature ```kotlin var cursorConfigScale: Float ``` |
| **cursorConfigScaleMultiplier** : Float [Get][Set] | Signature ```kotlin var cursorConfigScaleMultiplier: Float ``` |
| **cursorConfigZOffset** : Float [Get][Set] | Signature ```kotlin var cursorConfigZOffset: Float ``` |
| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| **isdkSystem** : [IsdkSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdksystem) [Get] | Signature ```kotlin val isdkSystem: IsdkSystem ``` |
| **laserConfigColorActuated** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | Signature ```kotlin var laserConfigColorActuated: Vector3 ``` |
| **laserConfigColorNormal** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | Signature ```kotlin var laserConfigColorNormal: Vector3 ``` |
| **laserConfigDefault** : IsdkDefaultCursorSystem.PerDeviceLaserConfig [Get][Set] | Signature ```kotlin var laserConfigDefault: IsdkDefaultCursorSystem.PerDeviceLaserConfig ``` |
| **laserConfigFadeTime** : Float [Get][Set] | Signature ```kotlin var laserConfigFadeTime: Float ``` |
| **laserConfigHand** : IsdkDefaultCursorSystem.PerDeviceLaserConfig [Get][Set] | Signature ```kotlin var laserConfigHand: IsdkDefaultCursorSystem.PerDeviceLaserConfig ``` |
| **laserConfigMaxLength** : Float [Get] | Signature ```kotlin val laserConfigMaxLength: Float = 0.25f ``` |
| **laserConfigWidth** : Float [Get][Set] | Signature ```kotlin var laserConfigWidth: Float ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |
| **unifiedCursorConfigRadiusLeastPinch** : Float [Get][Set] | Signature ```kotlin var unifiedCursorConfigRadiusLeastPinch: Float ``` |
| **unifiedCursorConfigRadiusMostPinch** : Float [Get][Set] | Signature ```kotlin var unifiedCursorConfigRadiusMostPinch: Float ``` |
| **unifiedCursorConfigScale** : Float [Get][Set] | Signature ```kotlin var unifiedCursorConfigScale: Float ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **delete** ( entity ) | System should do any housekeeping based on [SystemBase.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase#delete) being removed from the scene Signature ```kotlin open fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open override fun destroy() ``` |
| **enableInput** ( enabled ) | Signature ```kotlin fun enableInput(enabled: Boolean) ``` Parameters enabled: Boolean |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |

## Inner Class

### PerDeviceLaserConfig Class

*Modifiers:
final*

Signature
```kotlin
data class PerDeviceLaserConfig(val surfaceOffset: Float, val originOffset: Float, val farToNearFadeLength: Float, val nearToFarFadeLength: Float)
```

Constructors
| **PerDeviceLaserConfig** ( surfaceOffset , originOffset , farToNearFadeLength , nearToFarFadeLength ) | Signature ```kotlin constructor(surfaceOffset: Float, originOffset: Float, farToNearFadeLength: Float, nearToFarFadeLength: Float) ``` Parameters surfaceOffset: Float originOffset: Float farToNearFadeLength: Float nearToFarFadeLength: Float Returns IsdkDefaultCursorSystem.PerDeviceLaserConfig |
| --- | --- |

Properties
| **farToNearFadeLength** : Float [Get] | Signature ```kotlin val farToNearFadeLength: Float ``` |
| --- | --- |
| **nearToFarFadeLength** : Float [Get] | Signature ```kotlin val nearToFarFadeLength: Float ``` |
| **originOffset** : Float [Get] | Signature ```kotlin val originOffset: Float ``` |
| **surfaceOffset** : Float [Get] | Signature ```kotlin val surfaceOffset: Float ``` |