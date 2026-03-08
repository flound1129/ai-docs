# CachedQueryBuilder Class

*Modifiers:
final*

Builder for [CachedQuery](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery) expressions.

This builder provides a restricted DSL that only supports `has()` operations with `and` / `or` combinators. Filters, sorting, and other Query operations are intentionally not available to ensure efficient incremental updates.

Example:

```kotlin CachedQuery.create {
    where { has(Enemy.id) or has(Ally.id) }  // Use where as root (only one allowed)
} ```

## Signature

```kotlin
class CachedQueryBuilder
```

## Constructors

| **CachedQueryBuilder** () | Signature ```kotlin constructor() ``` Returns [CachedQueryBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerybuilder) |
| --- | --- |

## Functions

| **where** ( initializer ) | Creates a query using the `where` DSL block, matching the [Query.Companion.where](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_query#where) syntax. This provides a consistent API with [Query.Companion.where](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_query#where) for familiarity. Only one `where` block is allowed per query - nested `where` calls are prevented at compile time. The result of `where` has a `filter` method available, allowing filters to be applied only when `where` is used. Example: ```kotlin CachedQuery.create { where { has(Enemy.id, Health.id) } // Same as: has(Enemy.id, Health.id) } CachedQuery.create { where { has(Enemy.id) }.filter { by(Enemy.statusData).isEqualTo(Status.ACTIVE) } } ``` Signature ```kotlin fun where(initializer: CachedQueryWhereBuilder.() -> CachedQueryNode): FilteredCachedQueryNode.Unfiltered ``` Parameters initializer: Function1 Query DSL block that returns a [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) . Uses [CachedQueryWhereBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerywherebuilder) which does not have a `where` method, preventing nesting. Returns FilteredCachedQueryNode.Unfiltered A [FilteredCachedQueryNode.Unfiltered](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filteredcachedquerynode#unfiltered) which has a `filter` method for adding filters. |
| --- | --- |