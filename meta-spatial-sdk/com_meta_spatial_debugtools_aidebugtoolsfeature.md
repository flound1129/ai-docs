# AIDebugToolsFeature Class

Implements
[SpatialFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature)
*Modifiers:
final*

## Signature

```kotlin
class AIDebugToolsFeature(val activity: AppSystemActivity) : SpatialFeature
```

## Constructors

| **AIDebugToolsFeature** ( activity ) | Signature ```kotlin constructor(activity: AppSystemActivity) ``` Parameters activity: [AppSystemActivity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_appsystemactivity) Returns [AIDebugToolsFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_debugtools_aidebugtoolsfeature) |
| --- | --- |

## Properties

| **activity** : [AppSystemActivity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_appsystemactivity) [Get] | Signature ```kotlin val activity: AppSystemActivity ``` |
| --- | --- |

## Functions

| **componentsToRegister** () | Override this function to define a list of components that should be used by the application. Signature ```kotlin open fun componentsToRegister(): List<ComponentRegistration> ``` Returns List A list of ComponentRegistration objects representing the components to register. |
| --- | --- |
| **earlySystemsToRegister** () | Override this method to register your systems that should be executed with [PriorityGroup](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_prioritygroup) EARLY. Signature ```kotlin open fun earlySystemsToRegister(): List<SystemBase> ``` Returns List A list of SystemBase objects |
| **getDependencies** () | Override this method to define a list of dependencies required by this feature. This will be verified at runtime. Example: ```kotlin // MyCustomFeature.kt override fun getDependencies(): List<KClass<out SpatialFeature>> { return listOf(ToolkitFeature::class) } @return A list of SpatialFeature classes representing the dependencies. ``` Signature ```kotlin open fun getDependencies(): List<KClass<out SpatialFeature>> ``` Returns List |
| **lateSystemsToRegister** () | Override this method to register your systems that should be executed with [PriorityGroup](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_prioritygroup) LATE. Signature ```kotlin open fun lateSystemsToRegister(): List<SystemBase> ``` Returns List A list of SystemBase objects |
| **loadLibrary** ( libName ) | Loads a native library into the application. Signature ```kotlin open fun loadLibrary(libName: String) ``` Parameters libName: String The name of the library to load. |
| **onCreate** ( savedInstanceState ) | Called when the application is created. Override this method to perform actions during the OnCreate() lifecycle of the application. Signature ```kotlin open fun onCreate(savedInstanceState: Bundle?) ``` Parameters savedInstanceState: Bundle? The saved instance state of the application. |
| **onDestroy** () | Called when the application is in onDestroy callback. Be aware that onDestroy() is not guaranteed to be called. Override this method to perform actions during the OnDestroy() lifecycle of the application. Signature ```kotlin open fun onDestroy() ``` |
| **onPauseActivity** () | Called when the activity is in onPause callback. Override this method to perform actions during the OnPause() lifecycle of the application. Signature ```kotlin open fun onPauseActivity() ``` |
| **onResume** () | Called when the application is resumed. Override this method to perform actions during the OnResume() lifecycle of the application. Signature ```kotlin open fun onResume() ``` |
| **onSceneReady** () | Called when the scene is ready. Override this method to perform actions during the OnSceneReady() lifecycle of the application. Signature ```kotlin open override fun onSceneReady() ``` |
| **onSpatialShutdown** () | Called when the application is shutting down. Clean up all Spatial resources for your feature, e.g. entites.destroy(), in this callback. Signature ```kotlin open override fun onSpatialShutdown() ``` |
| **onStart** () | Called when the application is started. Override this method to perform actions during the OnStart() lifecycle of the application. Signature ```kotlin open fun onStart() ``` |
| **onStopActivity** () | Called when the activity is in onStop callback. Be aware that onStop() is not guaranteed to be called. Override this method to perform actions during the OnStop() lifecycle of the application. Signature ```kotlin open fun onStopActivity() ``` |
| **onVRPause** () | Called when the VR mode is paused. Override this method to perform actions during the OnVRPause() lifecycle of the application. Signature ```kotlin open fun onVRPause() ``` |
| **onVRReady** () | Called when the VR mode is ready. Override this method to perform actions during the onVRReady() lifecycle of the application. Signature ```kotlin open fun onVRReady() ``` |
| **preRuntimeOnCreate** ( savedInstanceState ) | Called before the application's onCreate() method is called. Override this method to perform actions before the rest of the OnCreate() lifecycle of the application. Signature ```kotlin open fun preRuntimeOnCreate(savedInstanceState: Bundle?) ``` Parameters savedInstanceState: Bundle? The saved instance state of the application. |
| **registerRequiredOpenXRExtensions** () | Override this function to define a list of required OpenXR extensions that should be enabled by your application. Signature ```kotlin open fun registerRequiredOpenXRExtensions(): List<String> ``` Returns List A list of strings representing the required OpenXR extensions. |
| **systemsToRegister** () | Override this method to register your systems that should be executed [PriorityGroup](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_prioritygroup) NORMAL. Signature ```kotlin open override fun systemsToRegister(): List<SystemBase> ``` Returns List A list of SystemBase objects |

## Inner Classes

### ClickResult Class

*Modifiers:
final*

Signature
```kotlin
data class ClickResult(val success: Boolean, val usedAccessibility: Boolean, val error: String? = null)
```

Constructors
| **ClickResult** ( success , usedAccessibility , error ) | Signature ```kotlin constructor(success: Boolean, usedAccessibility: Boolean, error: String? = null) ``` Parameters success: Boolean usedAccessibility: Boolean error: String? Returns AIDebugToolsFeature.ClickResult |
| --- | --- |

Properties
| **error** : String? [Get] | Signature ```kotlin val error: String? = null ``` |
| --- | --- |
| **success** : Boolean [Get] | Signature ```kotlin val success: Boolean ``` |
| **usedAccessibility** : Boolean [Get] | Signature ```kotlin val usedAccessibility: Boolean ``` |

### CommandResult Class

*Modifiers:
final*

Constructors
| **CommandResult** ( success , message , data ) | Signature ```kotlin constructor(success: Boolean, message: String, data: JSONObject?) ``` Parameters success: Boolean message: String data: JSONObject? Returns AIDebugToolsFeature.CommandResult |
| --- | --- |

Properties
| **data** : JSONObject? [Get] | Signature ```kotlin val data: JSONObject ``` |
| --- | --- |
| **message** : String [Get] | Signature ```kotlin val message: String ``` |
| **success** : Boolean [Get] | Signature ```kotlin val success: Boolean ``` |

Functions
| **toJson** () | Signature ```kotlin fun toJson(): String ``` Returns String |
| --- | --- |