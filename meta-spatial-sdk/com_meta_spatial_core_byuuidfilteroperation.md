# ByUUIDFilterOperation Class

*Modifiers:
final*

A class representing a filter operation for UUID attributes.

## Signature

```kotlin
class ByUUIDFilterOperation(val attrId: Int, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByUUIDFilterOperation** ( attrId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the filter operation. filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByUUIDFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byuuidfilteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | The attribute id of the filter operation. Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | The filter builder object used to create the filter node. Signature ```kotlin val filterBuilder: FilterBuilder ``` |

## Functions

| **isEqualTo** ( value ) | Creates a filter node representing an equality condition with the given UUID value. Signature ```kotlin fun isEqualTo(value: UUID): ByUUIDFilterNode ``` Parameters value: UUID The string value to compare against. Returns [ByUUIDFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byuuidfilternode) A filter node representing the equality condition. |
| --- | --- |