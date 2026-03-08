# DebugUtils Object

Debug utilities for testing native crashes and crash diagnostics.

These functions are intended for E2E testing of crash reporting infrastructure. They will cause the app to crash and should only be used in test builds.

## Signature

```kotlin
object DebugUtils
```

## Functions

| **nativeTriggerCrash** () | Triggers a native crash via null pointer dereference. This function is used to test crash reporting infrastructure (e.g., crashpad, tombstones) and verify that debug symbols produce readable stack traces. WARNING: This will crash the application. Only use in E2E tests. Signature ```kotlin external fun nativeTriggerCrash() ``` |
| --- | --- |
| **triggerCrash** () | Triggers a native crash for testing purposes. This is a convenience wrapper around [DebugUtils.nativeTriggerCrash](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_debugutils#nativetriggercrash) for Kotlin callers. Signature ```kotlin fun triggerCrash() ``` |