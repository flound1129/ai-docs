# AnimationTrack Class

*Modifiers:
final*

Represents an animation track, which is a sequence of animations that can be played back.

Can be retrieved from an entity via scene object.

```kotlin systemManager.findSystem<SceneObjectSystem>().getSceneObject(entity)?.thenAccept { so ->
    val animationTracks = so.mesh?.getAnimationTracks()
} ```

## Signature

```kotlin
class AnimationTrack(val id: Int, val name: String, val length: Float)
```

## Constructors

| **AnimationTrack** ( id , name , length ) | Signature ```kotlin constructor(id: Int, name: String, length: Float) ``` Parameters id: Int a unique identifier for the animation track name: String a human-readable name for the animation track length: Float the total length of the animation track in seconds Returns [AnimationTrack](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_animationtrack) |
| --- | --- |

## Properties

| **id** : Int [Get] | Signature ```kotlin val id: Int ``` |
| --- | --- |
| **length** : Float [Get] | Signature ```kotlin val length: Float ``` |
| **name** : String [Get] | Signature ```kotlin val name: String ``` |