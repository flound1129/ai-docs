# EventArgs Class

*Modifiers:
open*

## Signature

```kotlin
open class EventArgs(val eventName: String, val dataModel: DataModel, var handled: Boolean = false, var throttleTime: Int? = null)
```

## Constructors

| **EventArgs** ( eventName , dataModel , handled , throttleTime ) | Signature ```kotlin constructor(eventName: String, dataModel: DataModel, handled: Boolean = false, throttleTime: Int? = null) ``` Parameters eventName: String dataModel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) handled: Boolean throttleTime: Int? Returns [EventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_eventargs) |
| --- | --- |

## Properties

| **dataModel** : [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) [Get] | Signature ```kotlin val dataModel: DataModel ``` |
| --- | --- |
| **eventName** : String [Get] | Signature ```kotlin val eventName: String ``` |
| **handled** : Boolean [Get][Set] | Signature ```kotlin var handled: Boolean ``` |
| **throttleTime** : Int? [Get][Set] | Signature ```kotlin var throttleTime: Int? ``` |