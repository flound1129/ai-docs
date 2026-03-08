# SceneAudioPlayer Class

*Modifiers:
final*

Controls playback of spatial audio in a 3D scene with dynamic control capabilities.

Unlike the direct playSound methods in [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) , SceneAudioPlayer provides ongoing control over audio playback, allowing you to start, stop, and update properties like volume and position while the sound is playing.

Example usage:

```kotlin // Load an audio asset
val audioAsset = SceneAudioAsset.loadLocalFile("data/common/audio/ambient.ogg")
// Create an audio player for the asset
val audioPlayer = SceneAudioPlayer(scene, audioAsset)
// Play the sound at a specific position with looping enabled
audioPlayer.play(
    position = Vector3(0f, 1.7f, -2f),
    volume = 0.8f,
    looping = true
)
// Later, update the volume
audioPlayer.setVolume(0.5f)
// Move the sound to follow an object
audioPlayer.setPosition(objectPosition)
// Stop playback when no longer needed
audioPlayer.stop() ```

Each SceneAudioPlayer instance is assigned a unique channel name, allowing multiple sounds to be controlled independently.

## Signature

```kotlin
class SceneAudioPlayer
```

## Constructors

| **SceneAudioPlayer** ( scene , soundAsset ) | Creates a new audio player for the specified audio asset. Signature ```kotlin constructor(scene: Scene, soundAsset: SceneAudioAsset) ``` Parameters scene: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene in which to play the audio soundAsset: [SceneAudioAsset](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneaudioasset) The audio asset to play Returns [SceneAudioPlayer](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneaudioplayer) |
| --- | --- |

## Functions

| **play** ( position , volume , looping ) | Starts playing the audio at the specified position. Signature ```kotlin fun play(position: Vector3, volume: Float = 1.0f, looping: Boolean = false) ``` Parameters position: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The 3D position where the sound should originate from volume: Float The volume level from 0.0 (silent) to 1.0 (full volume) looping: Boolean Whether the audio should loop continuously |
| --- | --- |
| **setPosition** ( position ) | Updates the position of the currently playing audio. This can be used to move the sound source while it's playing, for example to follow a moving object in the scene. Signature ```kotlin fun setPosition(position: Vector3) ``` Parameters position: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The new 3D position for the sound source |
| **setVolume** ( volume ) | Adjusts the volume of the currently playing audio. Signature ```kotlin fun setVolume(volume: Float) ``` Parameters volume: Float The new volume level from 0.0 (silent) to 1.0 (full volume) |
| **stop** () | Stops the audio playback. Once stopped, the audio can be played again by calling [SceneAudioPlayer.play](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneaudioplayer#play) . Signature ```kotlin fun stop() ``` |

## Companion Object

### Companion Object Properties

| **playerCount** : Int [Get] | Signature ```kotlin var playerCount: Int ``` |
| --- | --- |