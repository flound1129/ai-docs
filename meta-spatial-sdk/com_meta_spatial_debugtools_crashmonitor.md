# CrashMonitor Object

Crash and exception monitoring utilities for AI debug tools.

Provides capabilities to:

- Monitor for crashes via logcat - Capture stack traces - Detect ANRs (Application Not Responding) - Export crash reports

## Signature

```kotlin
object CrashMonitor
```

## Functions

| **captureAllThreadStackTraces** () | Signature ```kotlin fun captureAllThreadStackTraces(): Map<String, List<String>> ``` Returns Map |
| --- | --- |
| **captureCurrentStackTrace** () | Signature ```kotlin fun captureCurrentStackTrace(): List<String> ``` Returns List |
| **clearHistory** () | Signature ```kotlin fun clearHistory() ``` |
| **exportCrashReport** () | Signature ```kotlin fun exportCrashReport(): JSONObject ``` Returns JSONObject |
| **getCrashHistory** () | Signature ```kotlin fun getCrashHistory(): List<CrashMonitor.CrashInfo> ``` Returns List |
| **getFirstCrash** () | Signature ```kotlin fun getFirstCrash(): CrashMonitor.CrashInfo? ``` Returns CrashMonitor.CrashInfo? |
| **getLastCrash** () | Signature ```kotlin fun getLastCrash(): CrashMonitor.CrashInfo? ``` Returns CrashMonitor.CrashInfo? |
| **install** ( packageName ) | Signature ```kotlin fun install(packageName: String) ``` Parameters packageName: String |
| **uninstall** () | Signature ```kotlin fun uninstall() ``` |

## Inner Class

### CrashInfo Class

*Modifiers:
final*

Signature
```kotlin
data class CrashInfo(val timestamp: Long, val exceptionType: String, val message: String, val stackTrace: List<String>, val threadName: String)
```

Constructors
| **CrashInfo** ( timestamp , exceptionType , message , stackTrace , threadName ) | Signature ```kotlin constructor(timestamp: Long, exceptionType: String, message: String, stackTrace: List<String>, threadName: String) ``` Parameters timestamp: Long exceptionType: String message: String stackTrace: List threadName: String Returns CrashMonitor.CrashInfo |
| --- | --- |

Properties
| **exceptionType** : String [Get] | Signature ```kotlin val exceptionType: String ``` |
| --- | --- |
| **message** : String [Get] | Signature ```kotlin val message: String ``` |
| **stackTrace** : List [Get] | Signature ```kotlin val stackTrace: List<String> ``` |
| **threadName** : String [Get] | Signature ```kotlin val threadName: String ``` |
| **timestamp** : Long [Get] | Signature ```kotlin val timestamp: Long ``` |

Functions
| **toJson** () | Signature ```kotlin fun toJson(): JSONObject ``` Returns JSONObject |
| --- | --- |