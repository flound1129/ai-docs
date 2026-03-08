# ByLongFilterOperation Class

*Modifiers:
final*

A class representing a filter operation for long integer attributes. It is used to build a filter expression by specifying comparison operations on long integer attributes.

This class provides methods for creating filter nodes that represent various comparison operations on long integer attributes, such as equality, greater than, less than, etc. These filter nodes can then be combined using logical operators (AND, OR) to create complex filtering conditions.

Example:

```kotlin // Find entities where longVar equals 1000L
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.longVarData).isEqualTo(1000L) }
// Find entities where longVar is between 500L and 1500L
Query.where { has(TestComponent.id) }
     .filter {
       by(TestComponent.longVarData).greaterThanOrEqualTo(500L) and
       by(TestComponent.longVarData).lessThanOrEqualTo(1500L)
     }
// Find entities where longVar is not equal to 0L
Query.where { has(TestComponent.id) }
     .filter { not(by(TestComponent.longVarData).isEqualTo(0L)) } ```

## Signature

```kotlin
class ByLongFilterOperation(val attrId: Int, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByLongFilterOperation** ( attrId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the long attribute for the filter operation. filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByLongFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bylongfilteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | The attribute id of the long attribute for the filter operation. Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | The filter builder object used to create the filter node. Signature ```kotlin val filterBuilder: FilterBuilder ``` |

## Functions

| **greaterThan** ( value ) | Creates a filter node representing a greater than condition with the given value. Signature ```kotlin fun greaterThan(value: Long): ByLongFilterNode ``` Parameters value: Long Returns [ByLongFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bylongfilternode) |
| --- | --- |
| **greaterThanOrEqualTo** ( value ) | Creates a filter node representing a greater than or equal to condition with the given value. Signature ```kotlin fun greaterThanOrEqualTo(value: Long): ByLongFilterNode ``` Parameters value: Long Returns [ByLongFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bylongfilternode) |
| **isEqualTo** ( value ) | Creates a filter node representing an equality condition with the given value. Signature ```kotlin fun isEqualTo(value: Long): ByLongFilterNode ``` Parameters value: Long Returns [ByLongFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bylongfilternode) |
| **lessThan** ( value ) | Creates a filter node representing a less than condition with the given value. Signature ```kotlin fun lessThan(value: Long): ByLongFilterNode ``` Parameters value: Long Returns [ByLongFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bylongfilternode) |
| **lessThanOrEqualTo** ( value ) | Creates a filter node representing a less than or equal to condition with the given value. Signature ```kotlin fun lessThanOrEqualTo(value: Long): ByLongFilterNode ``` Parameters value: Long Returns [ByLongFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bylongfilternode) |