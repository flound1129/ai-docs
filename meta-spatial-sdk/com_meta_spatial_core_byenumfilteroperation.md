# ByEnumFilterOperation Class

*Modifiers:
final*

A class representing a filter operation for Enum attributes. It is used to build a filter expression by specifying comparison and pattern matching operations on string attribute values.

Example:

```kotlin // Find entities where enumVar equals TestEnum.FOO
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.enumVarData).isEqualTo(TestEnum.FOO) } ```

## Signature

```kotlin
class ByEnumFilterOperation(val attrId: Int, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByEnumFilterOperation** ( attrId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the filter operation. filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByEnumFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byenumfilteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | The attribute id of the filter operation. Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | The filter builder object used to create the filter node. Signature ```kotlin val filterBuilder: FilterBuilder ``` |

## Functions

| **isEqualTo** ( enumValue ) | Creates a filter node representing an equality condition with the given Enum value. Signature ```kotlin fun isEqualTo(enumValue: Enum<*>): ByIntFilterNode ``` Parameters enumValue: Enum Returns [ByIntFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byintfilternode) A filter node representing the equality condition. |
| --- | --- |