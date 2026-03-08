# IsdkSystemNativeApi Class

*Modifiers:
open*

Wrapper around the native API calls. Provided as a separate class to allow for mocking in tests.

## Signature

```kotlin
open class IsdkSystemNativeApi
```

## Constructors

| **IsdkSystemNativeApi** () | Signature ```kotlin constructor() ``` Returns [IsdkSystemNativeApi](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdksystemnativeapi) |
| --- | --- |

## Functions

| **destroy** () | Signature ```kotlin open fun destroy() ``` |
| --- | --- |
| **enableDebugTools** ( enable ) | Signature ```kotlin open fun enableDebugTools(enable: Boolean) ``` Parameters enable: Boolean |
| **enableTransformers** ( enable ) | Signature ```kotlin open fun enableTransformers(enable: Boolean) ``` Parameters enable: Boolean |
| **getEventDecoratorId** ( decoratorName ) | Signature ```kotlin open fun getEventDecoratorId(decoratorName: String): Long ``` Parameters decoratorName: String Returns Long |
| **getEventDecoratorValueLong** ( pointerEventId , decoratorId ) | Signature ```kotlin open fun getEventDecoratorValueLong(pointerEventId: Int, decoratorId: Long): Long? ``` Parameters pointerEventId: Int decoratorId: Long Returns Long? |
| **init** ( sceneHandle ) | Signature ```kotlin open fun init(sceneHandle: Long) ``` Parameters sceneHandle: Long |
| **setScenePointerDistance** ( distance ) | Signature ```kotlin open fun setScenePointerDistance(distance: Float) ``` Parameters distance: Float |
| **tick** ( dataModel , deltaSeconds , currentTimeSeconds ) | Signature ```kotlin open fun tick(dataModel: Long, deltaSeconds: Double, currentTimeSeconds: Double): Array<PointerEvent>? ``` Parameters dataModel: Long deltaSeconds: Double currentTimeSeconds: Double Returns Array? |