# AIDebugAccessibilityService Class

*Modifiers:
final*

Minimal AccessibilityService for AI debugging automation.

This service enables text/ID-based UI element clicking for Jetpack Compose panels. When an AccessibilityService is active, Android's accessibility framework fully populates the accessibility tree, including Compose's semantic nodes which are otherwise lazy-loaded.

Enable via:

```kotlin adb shell settings put secure enabled_accessibility_services
    com.meta.spatial.debugtools/.AIDebugAccessibilityService
adb shell settings put secure accessibility_enabled 1 ```

Commands are received via broadcast:

- Action: com.meta.spatial.debugtools.ACCESSIBILITY_COMMAND - Commands: find_element, click_element, get_all_elements

## Signature

```kotlin
class AIDebugAccessibilityService
```

## Constructors

| **AIDebugAccessibilityService** () | Signature ```kotlin constructor() ``` Returns [AIDebugAccessibilityService](/reference/spatial-sdk/v0.10.1/com_meta_spatial_debugtools_aidebugaccessibilityservice) |
| --- | --- |

## Functions

| **onAccessibilityEvent** ( event ) | Signature ```kotlin open fun onAccessibilityEvent(event: AccessibilityEvent?) ``` Parameters event: AccessibilityEvent? |
| --- | --- |
| **onDestroy** () | Signature ```kotlin open fun onDestroy() ``` |
| **onInterrupt** () | Signature ```kotlin open fun onInterrupt() ``` |
| **onServiceConnected** () | Signature ```kotlin open fun onServiceConnected() ``` |

## Inner Class

### CommandResult Class

*Modifiers:
final*

Constructors
| **CommandResult** ( success , message , data ) | Signature ```kotlin constructor(success: Boolean, message: String, data: JSONObject?) ``` Parameters success: Boolean message: String data: JSONObject? Returns AIDebugAccessibilityService.CommandResult |
| --- | --- |

Properties
| **data** : JSONObject? [Get] | Signature ```kotlin val data: JSONObject ``` |
| --- | --- |
| **message** : String [Get] | Signature ```kotlin val message: String ``` |
| **success** : Boolean [Get] | Signature ```kotlin val success: Boolean ``` |

Functions
| **toJson** () | Signature ```kotlin fun toJson(): String ``` Returns String |
| --- | --- |