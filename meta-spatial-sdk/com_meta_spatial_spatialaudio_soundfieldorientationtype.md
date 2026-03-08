# SoundfieldOrientationType Enum

## Signature

```kotlin
enum SoundfieldOrientationType : Enum<SoundfieldOrientationType>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| POSITION | Soundfield orientation is determine by the relative position of the target Entity and head. |
| POSITION_Y_LOCKED | Soundfield orientation is determine by the relative position of the target Entity and head, however up/down movement (y axis) will not affect the sound. Useful if a user experience where the sound does not come from above/below the user is preferred. |
| ORIENTATION_ONLY | Soundfield orientation is determined purely by the orientations of the target Entity and head, only rotating the target entity will lead to a change in sound (changing the position will not). |