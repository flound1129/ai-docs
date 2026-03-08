# CachedQueryNode Class

AST node for CachedQuery expressions.

This sealed class represents the supported query operations for [CachedQuery](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery) . Only `has()` , `and` , and `or` operations are supported. Filters and other Query operations are intentionally not available.

## Signature

```kotlin
sealed class CachedQueryNode
```

## Functions

| **and** ( other ) | Combines this node with another using logical AND. Signature ```kotlin infix fun and(other: CachedQueryNode): CachedQueryNode ``` Parameters other: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) Returns [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) |
| --- | --- |
| **or** ( other ) | Combines this node with another using logical OR. Signature ```kotlin infix fun or(other: CachedQueryNode): CachedQueryNode ``` Parameters other: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) Returns [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) |

## Inner Classes

### Has Class

Extends
[CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode)
*Modifiers:
final*

Represents a `has(componentId, ...)` check.

Signature
```kotlin
data class Has(val componentIds: IntArray) : CachedQueryNode
```

Constructors
| **Has** ( componentIds ) | Signature ```kotlin constructor(componentIds: IntArray) ``` Parameters componentIds: IntArray Returns CachedQueryNode.Has |
| --- | --- |

Properties
| **componentIds** : IntArray [Get] | Signature ```kotlin val componentIds: IntArray ``` |
| --- | --- |

Functions
| **and** ( other ) | Combines this node with another using logical AND. Signature ```kotlin infix fun and(other: CachedQueryNode): CachedQueryNode ``` Parameters other: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) Returns [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) |
| --- | --- |
| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |
| **or** ( other ) | Combines this node with another using logical OR. Signature ```kotlin infix fun or(other: CachedQueryNode): CachedQueryNode ``` Parameters other: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) Returns [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) |

### And Class

Extends
[CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode)
*Modifiers:
final*

Represents a logical AND of two query nodes.

Signature
```kotlin
data class And(val left: CachedQueryNode, val right: CachedQueryNode) : CachedQueryNode
```

Constructors
| **And** ( left , right ) | Signature ```kotlin constructor(left: CachedQueryNode, right: CachedQueryNode) ``` Parameters left: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) right: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) Returns CachedQueryNode.And |
| --- | --- |

Properties
| **left** : [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) [Get] | Signature ```kotlin val left: CachedQueryNode ``` |
| --- | --- |
| **right** : [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) [Get] | Signature ```kotlin val right: CachedQueryNode ``` |

Functions
| **and** ( other ) | Combines this node with another using logical AND. Signature ```kotlin infix fun and(other: CachedQueryNode): CachedQueryNode ``` Parameters other: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) Returns [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) |
| --- | --- |
| **or** ( other ) | Combines this node with another using logical OR. Signature ```kotlin infix fun or(other: CachedQueryNode): CachedQueryNode ``` Parameters other: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) Returns [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) |

### Or Class

Extends
[CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode)
*Modifiers:
final*

Represents a logical OR of two query nodes.

Signature
```kotlin
data class Or(val left: CachedQueryNode, val right: CachedQueryNode) : CachedQueryNode
```

Constructors
| **Or** ( left , right ) | Signature ```kotlin constructor(left: CachedQueryNode, right: CachedQueryNode) ``` Parameters left: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) right: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) Returns CachedQueryNode.Or |
| --- | --- |

Properties
| **left** : [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) [Get] | Signature ```kotlin val left: CachedQueryNode ``` |
| --- | --- |
| **right** : [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) [Get] | Signature ```kotlin val right: CachedQueryNode ``` |

Functions
| **and** ( other ) | Combines this node with another using logical AND. Signature ```kotlin infix fun and(other: CachedQueryNode): CachedQueryNode ``` Parameters other: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) Returns [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) |
| --- | --- |
| **or** ( other ) | Combines this node with another using logical OR. Signature ```kotlin infix fun or(other: CachedQueryNode): CachedQueryNode ``` Parameters other: [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) Returns [CachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerynode) |