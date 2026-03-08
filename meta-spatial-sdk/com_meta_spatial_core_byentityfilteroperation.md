# ByEntityFilterOperation Class

*Modifiers:
final*

A class representing a filter operation for Entity attributes. It is used to build a filter expression by specifying equality operations on Entity attribute values.

This class provides a method for creating filter nodes that represent equality conditions on Entity attributes. These filter nodes can then be combined using logical operators (AND, OR) to create complex filtering conditions.

Example:

```kotlin // Find entities where entityVar equals a specific entity
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.entityVarData).isEqualTo(someEntity) }
// Find entities where entityVar is not equal to a specific entity
Query.where { has(TestComponent.id) }
     .filter { not(by(TestComponent.entityVarData).isEqualTo(someEntity)) } ```

## Signature

```kotlin
class ByEntityFilterOperation(val attrId: Int, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByEntityFilterOperation** ( attrId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the attribute of the filter operation. filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByEntityFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byentityfilteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | Signature ```kotlin val filterBuilder: FilterBuilder ``` |

## Functions

| **isEqualTo** ( value ) | Creates a filter node representing an equality condition with the given Entity value. Signature ```kotlin fun isEqualTo(value: Entity): ByEntityAttributeFilterNode ``` Parameters value: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The Entity value to compare against. Returns [ByEntityAttributeFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byentityattributefilternode) A filter node representing the equality condition. |
| --- | --- |