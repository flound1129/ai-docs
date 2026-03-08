# SpatialContext Class

*Modifiers:
final*

## Constructors

| **SpatialContext** ( ctx , spatial ) | Signature ```kotlin constructor(ctx: Context, spatial: SpatialInterface) ``` Parameters ctx: Context spatial: [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) Returns [SpatialContext](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialcontext) |
| --- | --- |

## Properties

| **spatial** : [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) [Get] | Signature ```kotlin val spatial: SpatialInterface ``` |
| --- | --- |

## Functions

| **getSystemService** ( name ) | Signature ```kotlin open fun getSystemService(name: String): Any? ``` Parameters name: String Returns Any? |
| --- | --- |
| **getSystemServiceName** ( serviceClass ) | Signature ```kotlin open fun getSystemServiceName(serviceClass: Class<*>): String? ``` Parameters serviceClass: Class Returns String? |