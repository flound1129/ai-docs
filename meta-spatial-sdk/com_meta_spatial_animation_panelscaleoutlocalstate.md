# PanelScaleOutLocalState Class

*Modifiers:
final*

## Signature

```kotlin
data class PanelScaleOutLocalState(val startTimeInMs: Long, val durationInMs: Long, val initialScale: Vector3, var isComplete: Boolean = false)
```

## Constructors

| **PanelScaleOutLocalState** ( startTimeInMs , durationInMs , initialScale , isComplete ) | Signature ```kotlin constructor(startTimeInMs: Long, durationInMs: Long, initialScale: Vector3, isComplete: Boolean = false) ``` Parameters startTimeInMs: Long durationInMs: Long initialScale: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) isComplete: Boolean Returns [PanelScaleOutLocalState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_animation_panelscaleoutlocalstate) |
| --- | --- |

## Properties

| **durationInMs** : Long [Get] | Signature ```kotlin val durationInMs: Long ``` |
| --- | --- |
| **initialScale** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | Signature ```kotlin val initialScale: Vector3 ``` |
| **isComplete** : Boolean [Get][Set] | Signature ```kotlin var isComplete: Boolean ``` |
| **startTimeInMs** : Long [Get] | Signature ```kotlin val startTimeInMs: Long ``` |