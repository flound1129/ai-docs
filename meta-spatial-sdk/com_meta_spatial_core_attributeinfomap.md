# AttributeInfoMap Class

*Modifiers:
final*

Data Class that holds a map of Attribute ID to Attribute Info. Version is bumped when it changes. Used in ComponentManager.

## Signature

```kotlin
data class AttributeInfoMap(val map: Map<Int, AttributeInfo> = mapOf(), val version: Int = 0)
```

## Constructors

| **AttributeInfoMap** ( map , version ) | Signature ```kotlin constructor(map: Map<Int, AttributeInfo> = mapOf(), version: Int = 0) ``` Parameters map: Map version: Int Returns [AttributeInfoMap](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_attributeinfomap) |
| --- | --- |

## Properties

| **map** : Map [Get] | Signature ```kotlin val map: Map<Int, AttributeInfo> ``` |
| --- | --- |
| **version** : Int [Get] | Signature ```kotlin val version: Int = 0 ``` |