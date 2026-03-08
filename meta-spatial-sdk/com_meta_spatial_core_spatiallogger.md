# SpatialLogger Object

Centralized logging utility for the Meta Spatial SDK that provides:

- Configurable log levels via `adb shell setprop debug.spatial.log.level <LEVEL>` - Structured, LLM-parseable log format with rich context - Category-based filtering for targeted debugging - Per-category log level overrides

Set the global log level using ADB:

```kotlin adb shell setprop debug.spatial.log.level VERBOSE  # Show all logs
adb shell setprop debug.spatial.log.level DEBUG    # Debug and above
adb shell setprop debug.spatial.log.level INFO     # Info and above (default)
adb shell setprop debug.spatial.log.level WARN     # Warnings and errors only
adb shell setprop debug.spatial.log.level ERROR    # Errors only
adb shell setprop debug.spatial.log.level NONE     # Disable all logging ```

Set per-category log levels:

```kotlin adb shell setprop debug.spatial.log.ECS VERBOSE    # Verbose for ECS category
adb shell setprop debug.spatial.log.PANEL DEBUG    # Debug for Panel category ```

Logs are output in a structured format designed for LLM parsing:

```kotlin [SPATIAL][category][timestamp] message | context_key=value context_key2=value2 ```

```kotlin // Simple logging
SpatialLogger.info(SpatialLogger.Category.ECS) { "Entity created" }
// With context for LLM parsing
SpatialLogger.info(SpatialLogger.Category.ECS) {
    "Entity created with components" to mapOf(
        "entityId" to entity.id,
        "componentCount" to components.size
    )
}
// Scoped logging for a specific class
class MySystem : SystemBase() {
    private val logger = SpatialLogger.scoped(SpatialLogger.Category.SYSTEM, "MySystem")
    override fun execute() {
        logger.debug { "Executing system" }
        logger.debug { "Processing entities" to mapOf("count" to queryEntities(query).count()) }
    }
}
// Performance timing with logging
SpatialLogger.timed(SpatialLogger.Category.PERF, "LoadMesh") {
    // expensive operation
} ```

## Signature

```kotlin
object SpatialLogger
```

## Functions

| **addLogCallback** ( callback ) | Registers a callback to receive all log events (for UI display, file logging, etc.) Signature ```kotlin fun addLogCallback(callback: SpatialLogger.LogCallback) ``` Parameters callback: SpatialLogger.LogCallback |
| --- | --- |
| **clearAllCategoryLevels** () | Clears all category-specific log level overrides Signature ```kotlin fun clearAllCategoryLevels() ``` |
| **clearCategoryLevel** ( category ) | Clears a category-specific log level override Signature ```kotlin fun clearCategoryLevel(category: SpatialLogger.Category) ``` Parameters category: SpatialLogger.Category |
| **debug** ( category , messageProvider ) | Log at DEBUG level with lazy message evaluation. ```kotlin SpatialLogger.debug(Category.ECS) { "Processing entities" to mapOf("count" to entities.size) } ``` Parameters category: SpatialLogger.Category messageProvider: Function0 |
| **debug** ( category , message ) | Log at DEBUG level - simple message without context Signature ```kotlin inline fun debug(category: SpatialLogger.Category, message: () -> String) ``` Parameters category: SpatialLogger.Category message: Function0 |
| **enter** ( category , methodName ) | Logs entry into a method/function. Use for tracing execution flow. ```kotlin override fun onCreate(savedInstanceState: Bundle?) { SpatialLogger.enter(SpatialLogger.Category.LIFECYCLE) { "MyActivity.onCreate" } // ... } ``` Signature ```kotlin inline fun enter(category: SpatialLogger.Category, crossinline methodName: () -> String) ``` Parameters category: SpatialLogger.Category methodName: Function0 |
| **error** ( category , messageProvider ) | Log at ERROR level with lazy message evaluation. ```kotlin SpatialLogger.error(Category.ECS) { "Failed to create entity" to mapOf("reason" to error) } ``` Parameters category: SpatialLogger.Category messageProvider: Function0 |
| **error** ( category , message ) | Log at ERROR level - simple message without context Signature ```kotlin inline fun error(category: SpatialLogger.Category, message: () -> String) ``` Parameters category: SpatialLogger.Category message: Function0 |
| **error** ( category , throwable , messageProvider ) | Log at ERROR level with exception and lazy message evaluation. ```kotlin SpatialLogger.error(Category.ECS, exception) { "Operation failed" to mapOf("op" to opName) } ``` Parameters category: SpatialLogger.Category throwable: Throwable messageProvider: Function0 |
| **exit** ( category , methodName ) | Logs exit from a method/function. Use for tracing execution flow. ```kotlin override fun onDestroy() { // ... SpatialLogger.exit(SpatialLogger.Category.LIFECYCLE) { "MyActivity.onDestroy" } } ``` Signature ```kotlin inline fun exit(category: SpatialLogger.Category, crossinline methodName: () -> String) ``` Parameters category: SpatialLogger.Category methodName: Function0 |
| **getEffectiveLevel** ( category ) | Returns the current effective log level for a category, considering both global level and category-specific overrides. Signature ```kotlin fun getEffectiveLevel(category: SpatialLogger.Category): SpatialLogger.Level ``` Parameters category: SpatialLogger.Category Returns SpatialLogger.Level |
| **info** ( category , messageProvider ) | Log at INFO level with lazy message evaluation. ```kotlin SpatialLogger.info(Category.LIFECYCLE) { "Activity created" to mapOf("name" to activityName) } ``` Parameters category: SpatialLogger.Category messageProvider: Function0 |
| **info** ( category , message ) | Log at INFO level - simple message without context Signature ```kotlin inline fun info(category: SpatialLogger.Category, message: () -> String) ``` Parameters category: SpatialLogger.Category message: Function0 |
| **invalidateLevelCache** () | Invalidates the cached log level, forcing a re-read from system properties Signature ```kotlin fun invalidateLevelCache() ``` |
| **isLoggable** ( level , category ) | Returns whether logging is enabled for the given level and category Signature ```kotlin fun isLoggable(level: SpatialLogger.Level, category: SpatialLogger.Category): Boolean ``` Parameters level: SpatialLogger.Level category: SpatialLogger.Category Returns Boolean |
| **removeLogCallback** ( callback ) | Removes a previously registered log callback Signature ```kotlin fun removeLogCallback(callback: SpatialLogger.LogCallback) ``` Parameters callback: SpatialLogger.LogCallback |
| **scoped** ( category , scopeName ) | Creates a scoped logger for a specific class/component. This is the preferred way to log from within a class, as it automatically includes the class name in logs. ```kotlin class MySystem : SystemBase() { private val logger = SpatialLogger.scoped(SpatialLogger.Category.SYSTEM, "MySystem") override fun execute() { logger.info("Processing entities", "count" to 42) } } ``` Signature ```kotlin fun scoped(category: SpatialLogger.Category, scopeName: String): SpatialLogger.ScopedLogger ``` Parameters category: SpatialLogger.Category scopeName: String Returns SpatialLogger.ScopedLogger |
| **setCategoryLevel** ( category , level ) | Sets a category-specific log level override (takes precedence over global level) Signature ```kotlin fun setCategoryLevel(category: SpatialLogger.Category, level: SpatialLogger.Level) ``` Parameters category: SpatialLogger.Category level: SpatialLogger.Level |
| **timed** ( category , operationName , block ) | Executes a block and logs its duration. Useful for performance profiling. ```kotlin SpatialLogger.timed(SpatialLogger.Category.PERF, "LoadMesh") { meshLoader.load(uri) } ``` Signature ```kotlin inline fun <T> timed(category: SpatialLogger.Category, operationName: String, block: () -> T): T ``` Parameters category: SpatialLogger.Category operationName: String block: Function0 Returns [SpatialLogger](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatiallogger) |
| **verbose** ( category , messageProvider ) | Log at VERBOSE level with lazy message evaluation. The message lambda is only evaluated if VERBOSE logging is enabled for this category, avoiding unnecessary string computation when logging is disabled. ```kotlin SpatialLogger.verbose(Category.ECS) { "Entity created" to mapOf("id" to entity.id) } ``` Parameters category: SpatialLogger.Category messageProvider: Function0 |
| **verbose** ( category , message ) | Log at VERBOSE level - simple message without context Signature ```kotlin inline fun verbose(category: SpatialLogger.Category, message: () -> String) ``` Parameters category: SpatialLogger.Category message: Function0 |
| **warn** ( category , messageProvider ) | Log at WARN level with lazy message evaluation. ```kotlin SpatialLogger.warn(Category.ECS) { "Component access issue" to mapOf("type" to typeName) } ``` Parameters category: SpatialLogger.Category messageProvider: Function0 |
| **warn** ( category , message ) | Log at WARN level - simple message without context Signature ```kotlin inline fun warn(category: SpatialLogger.Category, message: () -> String) ``` Parameters category: SpatialLogger.Category message: Function0 |

## Inner Interface

### LogCallback Interface

Callback interface for custom log destinations (e.g., file, analytics, UI)

Signature
```kotlin
fun interface LogCallback
```

Functions
| **onLog** ( level , category , tag , message , context , timestamp ) | Signature ```kotlin abstract fun onLog(level: SpatialLogger.Level, category: SpatialLogger.Category, tag: String, message: String, context: Map<String, Any?>, timestamp: Long) ``` Parameters level: SpatialLogger.Level category: SpatialLogger.Category tag: String message: String context: Map timestamp: Long |
| --- | --- |

## Inner Class

### ScopedLogger Class

*Modifiers:
final*

A logger scoped to a specific component/class for consistent tagging

Signature
```kotlin
class ScopedLogger(val category: SpatialLogger.Category, scopeName: String)
```

Constructors
| **ScopedLogger** ( category , scopeName ) | Signature ```kotlin constructor(category: SpatialLogger.Category, scopeName: String) ``` Parameters category: SpatialLogger.Category scopeName: String Returns SpatialLogger.ScopedLogger |
| --- | --- |

Properties
| **category** : SpatialLogger.Category [Get] | Signature ```kotlin val category: SpatialLogger.Category ``` |
| --- | --- |

Functions
| **debug** ( messageProvider ) | Log at DEBUG level with lazy message evaluation Parameters messageProvider: Function0 |
| --- | --- |
| **debug** ( message ) | Log at DEBUG level - simple message without context Signature ```kotlin inline fun debug(message: () -> String) ``` Parameters message: Function0 |
| **error** ( messageProvider ) | Log at ERROR level with lazy message evaluation Parameters messageProvider: Function0 |
| **error** ( message ) | Log at ERROR level - simple message without context Signature ```kotlin inline fun error(message: () -> String) ``` Parameters message: Function0 |
| **error** ( throwable , messageProvider ) | Log at ERROR level with exception and lazy message evaluation Parameters throwable: Throwable messageProvider: Function0 |
| **info** ( messageProvider ) | Log at INFO level with lazy message evaluation Parameters messageProvider: Function0 |
| **info** ( message ) | Log at INFO level - simple message without context Signature ```kotlin inline fun info(message: () -> String) ``` Parameters message: Function0 |
| **timed** ( operationName , block ) | Executes a block and logs its duration ```kotlin logger.timed("LoadAssets") { loadAllAssets() } ``` Signature ```kotlin inline fun <T> timed(operationName: String, block: () -> T): T ``` Parameters operationName: String block: Function0 Returns SpatialLogger.ScopedLogger |
| **verbose** ( messageProvider ) | Log at VERBOSE level with lazy message evaluation Parameters messageProvider: Function0 |
| **verbose** ( message ) | Log at VERBOSE level - simple message without context Signature ```kotlin inline fun verbose(message: () -> String) ``` Parameters message: Function0 |
| **warn** ( messageProvider ) | Log at WARN level with lazy message evaluation Parameters messageProvider: Function0 |
| **warn** ( message ) | Log at WARN level - simple message without context Signature ```kotlin inline fun warn(message: () -> String) ``` Parameters message: Function0 |

## Inner Enums

### Level Enum

Log levels in order of verbosity (most verbose first)

Signature
```kotlin
enum Level : Enum<SpatialLogger.Level>
```

Enumeration Constants
| Member |
| --- |
| VERBOSE |
| DEBUG |
| INFO |
| WARN |
| ERROR |
| NONE |

Properties
| **priority** : Int [Get] | Signature ```kotlin val priority: Int ``` |
| --- | --- |
| **shortName** : String [Get] | Signature ```kotlin val shortName: String ``` |

### Category Enum

Predefined log categories for consistent filtering and LLM context. Each category represents a major SDK subsystem.

Signature
```kotlin
enum Category : Enum<SpatialLogger.Category>
```

Enumeration Constants
| Member |
| --- |
| ECS |
| SYSTEM |
| SCENE |
| LIFECYCLE |
| PANEL |
| INPUT |
| GRAPHICS |
| MESH |
| TRANSFORM |
| PHYSICS |
| SPATIAL |
| ASSET |
| AUDIO |
| NETWORK |
| PERF |
| DEBUG |
| AVATAR |
| MR |
| ANIMATION |
| TOOLKIT |

Properties
| **description** : String [Get] | Signature ```kotlin val description: String ``` |
| --- | --- |
| **displayName** : String [Get] | Signature ```kotlin val displayName: String ``` |