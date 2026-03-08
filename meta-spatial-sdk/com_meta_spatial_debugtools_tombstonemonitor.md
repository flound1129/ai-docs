# TombstoneMonitor Object

Native crash detection via tombstones.

Monitors for native crashes (C++ crashes) via tombstone files.

## Signature

```kotlin
object TombstoneMonitor
```

## Functions

| **getLatestTombstone** () | Signature ```kotlin fun getLatestTombstone(): TombstoneMonitor.Tombstone? ``` Returns TombstoneMonitor.Tombstone? |
| --- | --- |
| **listRecentTombstones** () | Signature ```kotlin fun listRecentTombstones(): List<TombstoneMonitor.Tombstone> ``` Returns List |
| **readTombstone** ( filename ) | Signature ```kotlin fun readTombstone(filename: String): String? ``` Parameters filename: String Returns String? |

## Inner Class

### Tombstone Class

*Modifiers:
final*

Signature
```kotlin
data class Tombstone(val filename: String, val timestamp: Long, val size: Long)
```

Constructors
| **Tombstone** ( filename , timestamp , size ) | Signature ```kotlin constructor(filename: String, timestamp: Long, size: Long) ``` Parameters filename: String timestamp: Long size: Long Returns TombstoneMonitor.Tombstone |
| --- | --- |

Properties
| **filename** : String [Get] | Signature ```kotlin val filename: String ``` |
| --- | --- |
| **size** : Long [Get] | Signature ```kotlin val size: Long ``` |
| **timestamp** : Long [Get] | Signature ```kotlin val timestamp: Long ``` |

Functions
| **toJson** () | Signature ```kotlin fun toJson(): JSONObject ``` Returns JSONObject |
| --- | --- |