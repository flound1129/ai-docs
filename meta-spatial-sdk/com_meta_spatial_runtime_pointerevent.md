# PointerEvent Class

*Modifiers:
final*

Data class representing a pointer event.

## Signature

```kotlin
class PointerEvent(val source: Entity, val type: Int, val hitInfo: HitInfo, val scrollInfo: Vector2 = Vector2(), val semanticType: Int = SemanticType.Unknown.id, val pointerType: Int = 0, val eventId: Int = 0)
```

## Constructors

| **PointerEvent** ( source , type , hitInfo , scrollInfo , semanticType , pointerType , eventId ) | Signature ```kotlin constructor(source: Entity, type: Int, hitInfo: HitInfo, scrollInfo: Vector2 = Vector2(), semanticType: Int = SemanticType.Unknown.id, pointerType: Int = 0, eventId: Int = 0) ``` Parameters source: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity that received the pointer event. type: Int See PointerEventType enum hitInfo: [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) Hit information: 3D for 3D objects and 2D for panels. scrollInfo: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) Optional scroll amount (used for thumbstick scrolling). semanticType: Int See SemanticType enum. pointerType: Int eventId: Int Returns [PointerEvent](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_pointerevent) |
| --- | --- |

## Properties

| **eventId** : Int [Get] | Signature ```kotlin val eventId: Int = 0 ``` |
| --- | --- |
| **hitInfo** : [HitInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_hitinfo) [Get] | Signature ```kotlin val hitInfo: HitInfo ``` |
| **pointerType** : Int [Get] | Signature ```kotlin val pointerType: Int = 0 ``` |
| **scrollInfo** : [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) [Get] | Signature ```kotlin val scrollInfo: Vector2 ``` |
| **semanticType** : Int [Get] | Signature ```kotlin val semanticType: Int ``` |
| **source** : [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get] | Signature ```kotlin val source: Entity ``` |
| **type** : Int [Get] | Signature ```kotlin val type: Int ``` |