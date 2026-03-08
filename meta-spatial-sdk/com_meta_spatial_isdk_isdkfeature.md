# IsdkFeature Class

Implements
[SpatialFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature)
*Modifiers:
final*

## Constructors

| **IsdkFeature** ( ctx , spatial , systemManager , enableDebugTools ) | Signature ```kotlin constructor(ctx: Context, spatial: SpatialInterface, systemManager: SystemManager, enableDebugTools: Boolean = false) ``` Parameters ctx: Context spatial: [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) enableDebugTools: Boolean Returns [IsdkFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdkfeature) |
| --- | --- |

## Properties

| **ctx** : Context [Get] | Signature ```kotlin val ctx: Context ``` |
| --- | --- |
| **enableDebugTools** : Boolean [Get] | Signature ```kotlin val enableDebugTools: Boolean = false ``` |
| **spatial** : [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) [Get] | Signature ```kotlin val spatial: SpatialInterface ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get] | Signature ```kotlin val systemManager: SystemManager ``` |

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
| **onSceneReady** () | Called when the scene is ready. Override this method to perform actions during the OnSceneReady() lifecycle of the application. Signature ```kotlin open fun onSceneReady() ``` |
| **onSpatialShutdown** () | Called when the application is shutting down. Clean up all Spatial resources for your feature, e.g. entites.destroy(), in this callback. Signature ```kotlin open fun onSpatialShutdown() ``` |
| **onStart** () | Called when the application is started. Override this method to perform actions during the OnStart() lifecycle of the application. Signature ```kotlin open fun onStart() ``` |
| **onStopActivity** () | Called when the activity is in onStop callback. Be aware that onStop() is not guaranteed to be called. Override this method to perform actions during the OnStop() lifecycle of the application. Signature ```kotlin open fun onStopActivity() ``` |
| **onVRPause** () | Called when the VR mode is paused. Override this method to perform actions during the OnVRPause() lifecycle of the application. Signature ```kotlin open fun onVRPause() ``` |
| **onVRReady** () | Called when the VR mode is ready. Override this method to perform actions during the onVRReady() lifecycle of the application. Signature ```kotlin open fun onVRReady() ``` |
| **preRuntimeOnCreate** ( savedInstanceState ) | Called before the application's onCreate() method is called. Override this method to perform actions before the rest of the OnCreate() lifecycle of the application. Signature ```kotlin open fun preRuntimeOnCreate(savedInstanceState: Bundle?) ``` Parameters savedInstanceState: Bundle? The saved instance state of the application. |
| **registerRequiredOpenXRExtensions** () | Override this function to define a list of required OpenXR extensions that should be enabled by your application. Signature ```kotlin open fun registerRequiredOpenXRExtensions(): List<String> ``` Returns List A list of strings representing the required OpenXR extensions. |
| **systemsToRegister** () | Override this method to register your systems that should be executed [PriorityGroup](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_prioritygroup) NORMAL. Signature ```kotlin open fun systemsToRegister(): List<SystemBase> ``` Returns List A list of SystemBase objects |