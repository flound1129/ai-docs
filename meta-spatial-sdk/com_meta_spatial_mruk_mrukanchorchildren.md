# mrukAnchorChildren Function

*Modifiers:
final*

Retrieves all child anchor entities of a given parent entity.

This function queries all entities with [MRUKAnchor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukanchor) components and returns those that reference the specified entity as their parent anchor.

## Signature

```kotlin
fun mrukAnchorChildren(entity: Entity): List<Entity>
```

## Parameters

entity:
[Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity)
The parent entity to find children for
## Returns

List
A list of child entities that have this entity as their parent anchor