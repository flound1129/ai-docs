# CachedQueryFilterData Class

*Modifiers:
final*

Holds filter data for CachedQuery native filtering.

This class contains the compiled filter expression and value arrays that are passed to the native query evaluation.

## Signature

```kotlin
class CachedQueryFilterData(val filterList: IntArray?, val filterIntList: IntArray?, val filterLongList: LongArray?, val filterFloatList: FloatArray?, val filterStringList: Array<String>?)
```

## Constructors

| **CachedQueryFilterData** ( filterList , filterIntList , filterLongList , filterFloatList , filterStringList ) | Signature ```kotlin constructor(filterList: IntArray?, filterIntList: IntArray?, filterLongList: LongArray?, filterFloatList: FloatArray?, filterStringList: Array<String>?) ``` Parameters filterList: IntArray? filterIntList: IntArray? filterLongList: LongArray? filterFloatList: FloatArray? filterStringList: Array? Returns [CachedQueryFilterData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedqueryfilterdata) |
| --- | --- |

## Properties

| **filterFloatList** : FloatArray? [Get] | Signature ```kotlin val filterFloatList: FloatArray? ``` |
| --- | --- |
| **filterIntList** : IntArray? [Get] | Signature ```kotlin val filterIntList: IntArray? ``` |
| **filterList** : IntArray? [Get] | Signature ```kotlin val filterList: IntArray? ``` |
| **filterLongList** : LongArray? [Get] | Signature ```kotlin val filterLongList: LongArray? ``` |
| **filterStringList** : Array? [Get] | Signature ```kotlin val filterStringList: Array<String>? ``` |

## Companion Object

### Companion Object Functions

| **fromBuilder** ( builder ) | Creates filter data from a FilterBuilder. Signature ```kotlin fun fromBuilder(builder: FilterBuilder): CachedQueryFilterData ``` Parameters builder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) Returns [CachedQueryFilterData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedqueryfilterdata) |
| --- | --- |