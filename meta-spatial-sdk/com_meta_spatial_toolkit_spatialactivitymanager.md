# SpatialActivityManager Object

This object is used to manage the current activity. It is used to get a weak reference to the current activity and execute code on the current activity.

Example of getting a reference to the [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) or [SpatialContext](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialcontext) via the activity:

```kotlin SpatialActivityManager.getAppSystemActivity().getSystemManager().findSystem<MySystem>() // Grabs the system manager which provides access to all registered systems.
SpatialActivityManager.getAppSystemActivity().getSceneObject() // Grabs the scene ```

## Signature

```kotlin
object SpatialActivityManager
```

## Properties

| **currentActivity** : WeakReference? [Get][Set] | The current Spatial activity. Signature ```kotlin var currentActivity: WeakReference<AppSystemActivity>? ``` |
| --- | --- |

## Functions

| **executeOnAppSystemActivity** ( runnable ) | This function is used to execute a block of code on the current AppSystemActivity's main thread. If the current activity has not been set or has been garbage collected, it will throw an exception. Signature ```kotlin fun executeOnAppSystemActivity(runnable: (activity: AppSystemActivity) -> Unit) ``` Parameters runnable: Function1 The block of code to be executed on the current AppSystemActivity. |
| --- | --- |
| **executeOnVrActivity** ( runnable ) | This generic function is used to execute a block of code on the current activity's main thread. If the current activity has not been set or has been garbage collected, it will do nothing. Signature ```kotlin inline fun <T : AppSystemActivity> executeOnVrActivity(crossinline runnable: (activity: T) -> Unit) ``` Parameters runnable: Function1 The block of code to be executed on the current activity. |
| **getAppSystemActivity** () | This function is used to get the current activity. This allows you to specify your activity so that you can access data on it. If the current activity has not been set or has been garbage collected, it will return null. Otherwise, it will return the current activity and cast it to type AppSystemActivity. Signature ```kotlin fun getAppSystemActivity(): AppSystemActivity ``` Returns [AppSystemActivity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_appsystemactivity) |
| **getVrActivity** () | This generic function is used to get the current activity. This allows you to specify your activity so that you can access data on it. If the current activity has not been set or has been garbage collected, it will return null. Signature ```kotlin inline fun <T : AppSystemActivity> getVrActivity(): T ``` Returns [SpatialActivityManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_spatialactivitymanager) The current activity. |