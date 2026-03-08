# LogcatMonitor Object

Logcat monitoring for crash detection.

Monitors logcat output for crash indicators and ANRs.

## Signature

```kotlin
object LogcatMonitor
```

## Functions

| **captureANRs** ( packageName ) | Signature ```kotlin fun captureANRs(packageName: String): List<String> ``` Parameters packageName: String Returns List |
| --- | --- |
| **captureRecentCrashes** ( packageName , lines ) | Signature ```kotlin fun captureRecentCrashes(packageName: String, lines: Int = 500): List<LogcatMonitor.LogcatCrash> ``` Parameters packageName: String lines: Int Returns List |
| **exportLogcat** ( outputPath , lines ) | Signature ```kotlin fun exportLogcat(outputPath: String, lines: Int = 1000): Boolean ``` Parameters outputPath: String lines: Int Returns Boolean |

## Inner Class

### LogcatCrash Class

*Modifiers:
final*

Signature
```kotlin
data class LogcatCrash(val timestamp: Long, val pid: Int, val tid: Int, val level: String, val tag: String, val message: String, val stackTrace: List<String>)
```

Constructors
| **LogcatCrash** ( timestamp , pid , tid , level , tag , message , stackTrace ) | Signature ```kotlin constructor(timestamp: Long, pid: Int, tid: Int, level: String, tag: String, message: String, stackTrace: List<String>) ``` Parameters timestamp: Long pid: Int tid: Int level: String tag: String message: String stackTrace: List Returns LogcatMonitor.LogcatCrash |
| --- | --- |

Properties
| **level** : String [Get] | Signature ```kotlin val level: String ``` |
| --- | --- |
| **message** : String [Get] | Signature ```kotlin val message: String ``` |
| **pid** : Int [Get] | Signature ```kotlin val pid: Int ``` |
| **stackTrace** : List [Get] | Signature ```kotlin val stackTrace: List<String> ``` |
| **tag** : String [Get] | Signature ```kotlin val tag: String ``` |
| **tid** : Int [Get] | Signature ```kotlin val tid: Int ``` |
| **timestamp** : Long [Get] | Signature ```kotlin val timestamp: Long ``` |

Functions
| **toJson** () | Signature ```kotlin fun toJson(): JSONObject ``` Returns JSONObject |
| --- | --- |