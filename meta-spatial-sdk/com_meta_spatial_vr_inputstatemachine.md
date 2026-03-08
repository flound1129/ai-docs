# InputStateMachine Class

*Modifiers:
final*

## Signature

```kotlin
class InputStateMachine
```

## Constructors

| **InputStateMachine** () | Signature ```kotlin constructor() ``` Returns [InputStateMachine](/reference/spatial-sdk/v0.10.1/com_meta_spatial_vr_inputstatemachine) |
| --- | --- |

## Properties

| **scene** : [Scene?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) [Get][Set] | Signature ```kotlin var scene: Scene? ``` |
| --- | --- |

## Functions

| **updateState** ( intersection , controllerEntity , buttons , changed , selectButtonsMask ) | Signature ```kotlin fun updateState(intersection: HitInfo?, controllerEntity: Entity, buttons: Int, changed: Int, selectButtonsMask: Int) ``` Parameters intersection: [HitInfo?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) controllerEntity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) buttons: Int changed: Int selectButtonsMask: Int |
| --- | --- |