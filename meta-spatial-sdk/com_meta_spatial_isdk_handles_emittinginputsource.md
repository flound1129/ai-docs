# EmittingInputSource Class

*Modifiers:
final*

Information about an input source emitting hover/grab events.

## Signature

```kotlin
data class EmittingInputSource(val hoverPosition: Vector3, val degrabbed: Boolean)
```

## Constructors

| **EmittingInputSource** ( hoverPosition , degrabbed ) | Signature ```kotlin constructor(hoverPosition: Vector3, degrabbed: Boolean) ``` Parameters hoverPosition: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) World position of the hover point degrabbed: Boolean Whether this source was degrabbed by another controller grabbing Returns [EmittingInputSource](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_handles_emittinginputsource) |
| --- | --- |

## Properties

| **degrabbed** : Boolean [Get] | Whether this source was degrabbed by another controller grabbing Signature ```kotlin val degrabbed: Boolean ``` |
| --- | --- |
| **hoverPosition** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | World position of the hover point Signature ```kotlin val hoverPosition: Vector3 ``` |