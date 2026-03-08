# AudioPauseMode Enum

Controls when audio playback is automatically paused and resumed.

Developers can override [VrActivity.audioPauseMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_vractivity#audiopausemode) to select the appropriate mode for their application's needs.

## Signature

```kotlin
enum AudioPauseMode : Enum<AudioPauseMode>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| ACTIVITY_FOCUS | Audio is paused/resumed based on Android Activity lifecycle (onPause/onResume). This is the default behavior. Use this when you want audio to stop whenever the Activity goes to background, including when the system UI is shown. |
| OPENXR_FOCUS | Audio is paused/resumed based on OpenXR session focus state. Audio continues playing when the Activity is paused but the XR session still has focus, and pauses when the XR session loses focus (e.g., when another immersive app gains focus). Use this for immersive VR apps where you want audio to continue even when Android Activity focus is lost temporarily. |
| MANUAL | Audio is not automatically paused or resumed. The developer is responsible for calling [Scene.setAudioEnabled](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene#setaudioenabled) manually. Use this when you need full control over audio lifecycle, for example to implement custom pause logic or to keep audio playing in specific scenarios. |