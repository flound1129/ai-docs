# HitInfo Class

*Modifiers:
final*

Contains information about a ray intersection hit in a 3D scene.

When performing ray casting or intersection testing in a 3D scene, HitInfo objects are returned to provide detailed information about where and how the ray intersected with scene geometry.

HitInfo objects are typically obtained from methods like [Scene.lineSegmentIntersect](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene#linesegmentintersect) or [Scene.rayArcIntersect](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene#rayarcintersect) , and are included in button event arguments like [ButtonClickEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttonclickeventargs) and [ButtonDownEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_buttondowneventargs) .

Example usage:

```kotlin // Perform a ray cast from the controller position in the forward direction
val hitInfo = scene.lineSegmentIntersect(
    dataModel,
    controllerPosition,
    controllerPosition + (controllerForward * maxDistance)
)
// Check if something was hit
if (hitInfo != null) {
    // Access hit information
    val hitEntity = hitInfo.entity
    val hitPoint = hitInfo.point
    val hitNormal = hitInfo.normal
    val hitDistance = hitInfo.distance
    // Perform actions based on the hit
    if (hitEntity != null) {
        // Interact with the hit entity
    }
} ```

## Signature

```kotlin
class HitInfo(val entity: Entity?, val sceneObjectHandle: Long, val nodeId: Int, val meshElementId: Int, val distance: Float, val point: Vector3, val normal: Vector3, val textureCoordinate: Vector2)
```

## Constructors

| **HitInfo** ( entity , sceneObjectHandle , nodeId , meshElementId , distance , point , normal , textureCoordinate ) | Signature ```kotlin constructor(entity: Entity?, sceneObjectHandle: Long, nodeId: Int, meshElementId: Int, distance: Float, point: Vector3, normal: Vector3, textureCoordinate: Vector2) ``` Parameters entity: [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity that was hit, or null if no entity is associated with the SceneObject sceneObjectHandle: Long The handle of the SceneObject that was hit nodeId: Int The ID of the node in the SceneObject that was hit meshElementId: Int The ID of the mesh element (e.g., triangle) that was hit distance: Float The distance from the interactor (controller, etc.) to the hit point point: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The 3D position of the hit point in world space normal: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The surface normal at the hit point in world space textureCoordinate: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The UV texture coordinate at the hit point Returns [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) |
| --- | --- |

## Properties

| **distance** : Float [Get] | The distance from the interactor (controller, etc.) to the hit point Signature ```kotlin val distance: Float ``` |
| --- | --- |
| **entity** : [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get] | The entity that was hit, or null if no entity is associated with the SceneObject Signature ```kotlin val entity: Entity? ``` |
| **meshElementId** : Int [Get] | The ID of the mesh element (e.g., triangle) that was hit Signature ```kotlin val meshElementId: Int ``` |
| **nodeId** : Int [Get] | The ID of the node in the SceneObject that was hit Signature ```kotlin val nodeId: Int ``` |
| **normal** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | The surface normal at the hit point in world space Signature ```kotlin val normal: Vector3 ``` |
| **point** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | The 3D position of the hit point in world space Signature ```kotlin val point: Vector3 ``` |
| **sceneObjectHandle** : Long [Get] | The handle of the SceneObject that was hit Signature ```kotlin val sceneObjectHandle: Long ``` |
| **textureCoordinate** : [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) [Get] | The UV texture coordinate at the hit point Signature ```kotlin val textureCoordinate: Vector2 ``` |