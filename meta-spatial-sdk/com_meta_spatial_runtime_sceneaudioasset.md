# SceneAudioAsset Class

*Modifiers:
final*

Represents an audio asset that can be played in a 3D scene.

SceneAudioAsset provides a way to load audio files and play them in the scene, either at specific 3D positions, attached to entities, or as background audio.

Example usage:

```kotlin // Load an audio file
val audioAsset = SceneAudioAsset.loadLocalFile("data/common/audio/click.ogg")
// Play the sound at a specific position in 3D space
scene.playSound(audioAsset, Vector3(0f, 1.7f, -1f), volume = 0.8f)
// Play the sound attached to an entity
scene.playSound(audioAsset, myEntity, volume = 1.0f)
// Play the sound attached to the user (non-spatialized)
scene.playSound(audioAsset, volume = 0.5f)
// Play looping background music
scene.playBackgroundSound(audioAsset, volume = 0.3f, looping = true)
// When done with the asset, release resources
audioAsset.destroy() ```

## Signature

```kotlin
class SceneAudioAsset
```

## Properties

| **canBeSpatialized** : Boolean [Get] | Whether the audio can be positioned in 3D space Signature ```kotlin val canBeSpatialized: Boolean ``` |
| --- | --- |
| **duration** : Float [Get] | Length of the audio in seconds Signature ```kotlin val duration: Float ``` |
| **handle** : Long [Get] | Native handle to the audio asset Signature ```kotlin var handle: Long ``` |
| **spatialInterface_** : [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) [Get] | Signature ```kotlin val spatialInterface_: SpatialInterface ``` |

## Functions

| **destroy** () | Signature ```kotlin fun destroy() ``` |
| --- | --- |

## Companion Object

### Companion Object Properties

| **spatialInterface** : [SpatialInterface?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) [Get][Set] | Signature ```kotlin var spatialInterface: SpatialInterface? ``` |
| --- | --- |

### Companion Object Functions

| **loadLocalFile** ( filename ) | Loads an audio file from the local filesystem. The file path is relative to the application's asset directory. OGG and WAV formats supported. Signature ```kotlin fun loadLocalFile(filename: String): SceneAudioAsset ``` Parameters filename: String Path to the audio file relative to the app's asset directory Returns [SceneAudioAsset](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneaudioasset) A new SceneAudioAsset instance |
| --- | --- |