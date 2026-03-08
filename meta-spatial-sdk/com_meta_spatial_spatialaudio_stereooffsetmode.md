# StereoOffsetMode Enum

## Signature

```kotlin
enum StereoOffsetMode : Enum<StereoOffsetMode>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| WORLD_SPACE | Stereo Offsets are positioned in absolute world space. They do not take into account the Entity's position. |
| LOCAL_SPACE | Stereo Offsets are positioned relative to the Entity's local space. If the Entity has no Transform, the offsets are positioned in world space. |
| HEAD_LOCKED | Stereo Offsets are positioned relative to the user's head. This does not take into account the Entity's position. |
| HEAD_RELATIVE | Stereo Offsets are positioned relative to the user's head but rotate with the Entity's orientation. |