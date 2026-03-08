# MainThreadCleanup Object

Utility for safely cleaning up objects that require main thread destruction.

This solves the problem where finalize() posts a destroy call to the main thread, but the object may be GC'd before the destroy runs. This utility holds a strong reference to the object until the cleanup completes on the main thread.

## Signature

```kotlin
object MainThreadCleanup
```

## Functions

| **scheduleCleanup** ( obj , cleanup ) | Schedule cleanup on the main thread while keeping the object alive. Signature ```kotlin fun <T : Any> scheduleCleanup(obj: T, cleanup: (T) -> Unit) ``` Parameters obj: [MainThreadCleanup](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_mainthreadcleanup) The object to keep alive during cleanup cleanup: Function1 The cleanup function to run on the main thread |
| --- | --- |