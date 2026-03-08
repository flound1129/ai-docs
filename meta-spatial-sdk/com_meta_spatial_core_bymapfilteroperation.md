# ByMapFilterOperation Class

*Modifiers:
final*

A class representing a filter operation for Map attributes. It is used to build a filter expression by specifying key-based operations on Map attribute values.

This class provides methods for creating filter nodes that represent operations on Map attributes, such as checking if a map contains a specific key. These filter nodes can then be combined using logical operators (AND, OR) to create complex filtering conditions.

Example:

```kotlin // Find entities where intToStringMap contains key 42
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.intToStringMapVarData).containsKey(42) }
// Find entities where stringToIntMap contains either "foo" or "bar" keys
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.stringToIntMapVarData).containsKey("foo") or
               by(TestComponent.stringToIntMapVarData).containsKey("bar") } ```

## Signature

```kotlin
class ByMapFilterOperation<KeyType, ValueType>(val attrId: Int, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByMapFilterOperation** ( attrId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the filter operation. filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByMapFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bymapfilteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | Signature ```kotlin val filterBuilder: FilterBuilder ``` |

## Functions

| **containsKey** ( key ) | Creates a filter node representing a condition that checks if a map contains a specific key. Signature ```kotlin fun containsKey(key: KeyType): ByMapFilterNode<KeyType, ValueType> ``` Parameters key: [ByMapFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bymapfilteroperation) The key to check for in the map. Returns [ByMapFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bymapfilternode) A filter node representing the condition. |
| --- | --- |