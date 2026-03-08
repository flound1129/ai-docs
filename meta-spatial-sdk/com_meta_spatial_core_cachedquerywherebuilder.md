# CachedQueryWhereBuilder Class

*Modifiers:
final*

Inner builder for [CachedQuery](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery) expressions within a `where` block.

This builder provides only `has()` operations with `and` / `or` combinators. It intentionally does NOT have a `where` method to prevent nested `where` blocks.

## Signature

```kotlin
class CachedQueryWhereBuilder
```

## Constructors

| **CachedQueryWhereBuilder** () | Signature ```kotlin constructor() ``` Returns [CachedQueryWhereBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerywherebuilder) |
| --- | --- |

## Functions

| **has** ( componentIds ) | Creates a query node that matches entities with all specified components. Signature ```kotlin fun has(vararg componentIds: Int): CachedQueryNode ``` Parameters componentIds: Int The component IDs to check for (e.g., `Enemy.id` , `Health.id` ). Returns [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) A query node representing the `has` check. |
| --- | --- |