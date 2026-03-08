# IsdkSceneObjectPool Class

*Modifiers:
final*

Internal class for managing the lifetime of SceneObjects used by the IsdkDefaultCursorSystem. Each SceneObject has a Mesh, returned by the meshFactory. The scene objects will not be frustum culled. It is not possible to return just a single SceneObject - calling reset() will mark all scene objects as returned.

## Signature

```kotlin
class IsdkSceneObjectPool(scene: Scene, meshFactory: () -> SceneMesh, namePrefix: String)
```

## Constructors

| **IsdkSceneObjectPool** ( scene , meshFactory , namePrefix ) | Signature ```kotlin constructor(scene: Scene, meshFactory: () -> SceneMesh, namePrefix: String) ``` Parameters scene: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) meshFactory: Function0 namePrefix: String Returns [IsdkSceneObjectPool](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdksceneobjectpool) |
| --- | --- |

## Functions

| **borrow** () | Borrows a SceneObject from the pool. If all SceneObjects are in use, a new one is created. Signature ```kotlin fun borrow(): SceneObject ``` Returns [SceneObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneobject) SceneObject - the borrowed SceneObject. |
| --- | --- |
| **destroy** () | Destroys all SceneObjects in the pool. Signature ```kotlin fun destroy() ``` |
| **getBorrowedCount** () | Returns the count of currently borrowed SceneObjects. Signature ```kotlin fun getBorrowedCount(): Int ``` Returns Int Int - the number of SceneObjects currently in use. |
| **reset** () | Resets the pool by making all borrowed SceneObjects invisible and resetting the used count. Signature ```kotlin fun reset() ``` |