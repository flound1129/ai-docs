# SplatLoadEventArgs Class

Extends
[EventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_eventargs)
*Modifiers:
final*

Event args for when a Splat completes loading

## Signature

```kotlin
class SplatLoadEventArgs(val success: Boolean, val errorMessage: String? = null, val dataModel: DataModel) : EventArgs
```

## Constructors

| **SplatLoadEventArgs** ( success , errorMessage , dataModel ) | Signature ```kotlin constructor(success: Boolean, errorMessage: String? = null, dataModel: DataModel) ``` Parameters success: Boolean Whether the load was successful errorMessage: String? Optional error message if load failed dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) Returns [SplatLoadEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_splat_splatloadeventargs) |
| --- | --- |

## Properties

| **dataModel** : [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) [Get] | Signature ```kotlin val dataModel: DataModel ``` |
| --- | --- |
| **errorMessage** : String? [Get] | Optional error message if load failed Signature ```kotlin val errorMessage: String? = null ``` |
| **eventName** : String [Get] | Signature ```kotlin val eventName: String ``` |
| **handled** : Boolean [Get][Set] | Signature ```kotlin var handled: Boolean ``` |
| **success** : Boolean [Get] | Whether the load was successful Signature ```kotlin val success: Boolean ``` |
| **throttleTime** : Int? [Get][Set] | Signature ```kotlin var throttleTime: Int? ``` |

## Companion Object

### Companion Object Properties

| **EVENT_NAME** : String [Get] | Signature ```kotlin const val EVENT_NAME: String ``` |
| --- | --- |

### Companion Object Functions

| **failure** ( errorMessage , dataModel ) | Signature ```kotlin fun failure(errorMessage: String, dataModel: DataModel): SplatLoadEventArgs ``` Parameters errorMessage: String dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) Returns [SplatLoadEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_splat_splatloadeventargs) |
| --- | --- |
| **success** ( dataModel ) | Signature ```kotlin fun success(dataModel: DataModel): SplatLoadEventArgs ``` Parameters dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) Returns [SplatLoadEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_splat_splatloadeventargs) |