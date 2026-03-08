# BlendMode Enum

Enum class representing the blending modes for rendering.

This enum defines how the colors of a material are blended with the background or other materials during rendering.

## Signature

```kotlin
enum BlendMode : Enum<BlendMode>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| OPAQUE | No blending is performed. This is the fastest and enables depth buffering. |
| TRANSLUCENT | This mode performs classic alpha blending, where the material's color is blended with the background based on its alpha value. |
| ADDITIVE | In this mode, all channels (red, green, blue, and alpha) are added together. |
| NONE | No color is written for the material. |
| DEPTH_TRANSITION_CUTAWAY |  |
| LAYER_TINT |  |

## Properties

| **mode** : Int [Get] | Signature ```kotlin val mode: Int ``` |
| --- | --- |