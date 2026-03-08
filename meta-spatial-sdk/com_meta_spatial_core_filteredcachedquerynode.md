# FilteredCachedQueryNode Class

Result of applying a filter to a CachedQueryNode.

This sealed class represents a query node with an optional filter attached. It allows the DSL syntax `where { has(...) }.filter { ... }` .

## Signature

```kotlin
sealed class FilteredCachedQueryNode
```

## Properties

| **filterData** : [CachedQueryFilterData?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedqueryfilterdata) [Get] | Signature ```kotlin abstract val filterData: CachedQueryFilterData? ``` |
| --- | --- |
| **queryNode** : [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) [Get] | Signature ```kotlin abstract val queryNode: CachedQueryNode ``` |

## Inner Classes

### Unfiltered Class

Extends
[FilteredCachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filteredcachedquerynode)
*Modifiers:
final*

A query node without a filter, returned by `where { ... }` .

This class has the `filter` method, ensuring filters can only be applied after using `where` .

Signature
```kotlin
data class Unfiltered(val queryNode: CachedQueryNode) : FilteredCachedQueryNode
```

Constructors
| **Unfiltered** ( queryNode ) | Signature ```kotlin constructor(queryNode: CachedQueryNode) ``` Parameters queryNode: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) Returns FilteredCachedQueryNode.Unfiltered |
| --- | --- |

Properties
| **filterData** : [CachedQueryFilterData?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedqueryfilterdata) [Get] | Signature ```kotlin open override val filterData: CachedQueryFilterData? = null ``` |
| --- | --- |
| **queryNode** : [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) [Get] | Signature ```kotlin open override val queryNode: CachedQueryNode ``` |

Functions
| **filter** ( initializer ) | Applies a filter to this query node. Filters are evaluated at the native level for both initial queries and incremental updates. Only entities that match both the query criteria AND the filter condition will be included. Example: ```kotlin CachedQuery.create { where { has(Enemy.id) }.filter { by(Enemy.statusData).isEqualTo(Status.ACTIVE) } } ``` Signature ```kotlin fun filter(initializer: FilterBuilder.() -> FilterNode): FilteredCachedQueryNode.Filtered ``` Parameters initializer: Function1 Filter DSL block using [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) syntax. Returns FilteredCachedQueryNode.Filtered A [FilteredCachedQueryNode.Filtered](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filteredcachedquerynode#filtered) containing this query node and the filter data. |
| --- | --- |

### Filtered Class

Extends
[FilteredCachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filteredcachedquerynode)
*Modifiers:
final*

A query node with a filter attached.

Signature
```kotlin
data class Filtered(val queryNode: CachedQueryNode, val filterData: CachedQueryFilterData) : FilteredCachedQueryNode
```

Constructors
| **Filtered** ( queryNode , filterData ) | Signature ```kotlin constructor(queryNode: CachedQueryNode, filterData: CachedQueryFilterData) ``` Parameters queryNode: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) filterData: [CachedQueryFilterData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedqueryfilterdata) Returns FilteredCachedQueryNode.Filtered |
| --- | --- |

Properties
| **filterData** : [CachedQueryFilterData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedqueryfilterdata) [Get] | Signature ```kotlin open override val filterData: CachedQueryFilterData ``` |
| --- | --- |
| **queryNode** : [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) [Get] | Signature ```kotlin open override val queryNode: CachedQueryNode ``` |