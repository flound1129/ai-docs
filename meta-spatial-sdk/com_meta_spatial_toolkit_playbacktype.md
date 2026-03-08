# PlaybackType Enum

Playback type of the animation. This is used to determine how the animation is played.

## Signature

```kotlin
enum PlaybackType : Enum<PlaybackType>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| LOOP | Restarts the animation at the beginning when it finishes |
| CLAMP | Plays animation once and then freezes at last keyframe |
| BOUNCE | Starts playing animation forward and then in reverse when it finishes |
| REVERSE_LOOP | Plays animation in reverse forever |