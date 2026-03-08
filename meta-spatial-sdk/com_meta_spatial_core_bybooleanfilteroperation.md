# ByBooleanFilterOperation Class

*Modifiers:
final*

A class representing a filter operation for boolean attributes. It is used to build a filter expression by specifying equality operations on boolean attribute values.

This class provides a method for creating filter nodes that represent equality conditions on boolean attributes. These filter nodes can then be combined using logical operators (AND, OR) to create complex filtering conditions.

Example:

```kotlin // Find entities where boolVar is true
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.boolVarData).isEqualTo(true) }
// Find entities where boolVar is false
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.boolVarData).isEqualTo(false) } ```

## Signature

```kotlin
class ByBooleanFilterOperation(val attrId: Int, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByBooleanFilterOperation** ( attrId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the filter operation. filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByBooleanFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bybooleanfilteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | The attribute id of the filter operation. Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | The filter builder object used to create the filter node. Signature ```kotlin val filterBuilder: FilterBuilder ``` |

## Functions

| **isEqualTo** ( boolValue ) | Creates a filter node representing an equality condition with the given value. Signature ```kotlin fun isEqualTo(boolValue: Boolean): ByIntFilterNode ``` Parameters boolValue: Boolean The boolean value to compare against. Returns [ByIntFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byintfilternode) |
| --- | --- |