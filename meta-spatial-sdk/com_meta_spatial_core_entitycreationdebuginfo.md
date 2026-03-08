# EntityCreationDebugInfo Class

*Modifiers:
final*

Holds debug information captured at entity creation time.

## Signature

```kotlin
data class EntityCreationDebugInfo(val callstack: String?, val creationTimeMs: Long)
```

## Constructors

| **EntityCreationDebugInfo** ( callstack , creationTimeMs ) | Signature ```kotlin constructor(callstack: String?, creationTimeMs: Long) ``` Parameters callstack: String? The formatted callstack at creation time, or null if capture was disabled. creationTimeMs: Long The creation timestamp in milliseconds (from SystemClock.elapsedRealtime). Returns [EntityCreationDebugInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entitycreationdebuginfo) |
| --- | --- |

## Properties

| **callstack** : String? [Get] | The formatted callstack at creation time, or null if capture was disabled. Signature ```kotlin val callstack: String? ``` |
| --- | --- |
| **creationTimeMs** : Long [Get] | The creation timestamp in milliseconds (from SystemClock.elapsedRealtime). Signature ```kotlin val creationTimeMs: Long ``` |

## Functions

| **formatTimeAlive** () | Formats the time alive as a human-readable string. Signature ```kotlin fun formatTimeAlive(): String ``` Returns String A formatted string like "1.234s" or "45.678s". |
| --- | --- |
| **getTimeAliveMs** () | Returns the time in milliseconds since this entity was created. Signature ```kotlin fun getTimeAliveMs(): Long ``` Returns Long The time alive in milliseconds. |