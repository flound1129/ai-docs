# EntityContext Object

This class is a singleton that provides access to the SpatialSDK specific objects such as the DataModel, SystemManager, and ComponentManager.

## Signature

```kotlin
object EntityContext
```

## Properties

| **getBaseHref** : Function0 [Get][Set] | Used to get the base href for your SpatialSDK instance. This is used to access files that are stored on device for your Spatial SDK app. Do not change this variable, only invoke it to get the base href. Signature ```kotlin var getBaseHref: Function0 ``` |
| --- | --- |
| **getComponentManager** : Function0 [Get][Set] | Used to get the ComponentManager object for your SpatialSDK instance. Do not change this variable, only invoke it to get the ComponentManager. Signature ```kotlin var getComponentManager: () -> ComponentManager? ``` |
| **getDataModel** : Function0 [Get][Set] | Used to get the DataModel object for your SpatialSDK instance. Do not change this variable, only invoke it to get the DataModel. Signature ```kotlin var getDataModel: () -> DataModel? ``` |
| **getSystemManager** : Function0 [Get][Set] | Used to get the SystemManager object for your SpatialSDK instance. Do not change this variable, only invoke it to get the SystemManager. Signature ```kotlin var getSystemManager: () -> SystemManager? ``` |