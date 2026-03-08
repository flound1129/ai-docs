# ToolkitFeature Class

Implements
[SpatialFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature)
*Modifiers:
final*

ToolkitFeature is a [SpatialFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature) that provides core toolkit functionality for Spatial SDK applications. This feature is registered by default in [AppSystemActivity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_appsystemactivity) , so you do not need to manually register it in your registerFeatures() method

The ToolkitFeature registers essential systems and components that provide common functionality for spatial applications, including:

- Mesh creation through the [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) component - Panel creation through the [Panel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panel) component - Audio playback - Input handling - Animation - Transformation and scaling via the [Transform](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_transform) and [Scale](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_scale) components - Visibility control with the [Visible](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_visible) component - [Grabbable](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_grabbable) objects - [Followable](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_followable) objects - GLXF asset loading and management - Other Default Spatial SDK Functionality

## Constructors

| **ToolkitFeature** ( glXFManager , spatial , systemManager , ctx ) | Signature ```kotlin constructor(glXFManager: GLXFManager, spatial: SpatialInterface, systemManager: SystemManager, ctx: Context) ``` Parameters glXFManager: [GLXFManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfmanager) The GLXF manager for handling GLXF assets spatial: [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) The spatial interface for interacting with the spatial runtime systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager for registering systems ctx: Context The Android context (generally your Spatial SDK Immersive Activity) Returns [ToolkitFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_toolkitfeature) |
| --- | --- |

## Properties

| **glXFManager** : [GLXFManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfmanager) [Get] | The GLXF manager for handling GLXF assets Signature ```kotlin val glXFManager: GLXFManager ``` |
| --- | --- |

## Functions

| **getDependencies** () | Override this method to define a list of dependencies required by this feature. This will be verified at runtime. Example: ```kotlin // MyCustomFeature.kt override fun getDependencies(): List<KClass<out SpatialFeature>> { return listOf(ToolkitFeature::class) } @return A list of SpatialFeature classes representing the dependencies. ``` Signature ```kotlin open fun getDependencies(): List<KClass<out SpatialFeature>> ``` Returns List |
| --- | --- |
| **loadLibrary** ( libName ) | Loads a native library into the application. Signature ```kotlin open fun loadLibrary(libName: String) ``` Parameters libName: String The name of the library to load. |
| **onCreate** ( savedInstanceState ) | Called when the application is created. Override this method to perform actions during the OnCreate() lifecycle of the application. Signature ```kotlin open fun onCreate(savedInstanceState: Bundle?) ``` Parameters savedInstanceState: Bundle? The saved instance state of the application. |
| **onDestroy** () | Called when the application is in onDestroy callback. Be aware that onDestroy() is not guaranteed to be called. Override this method to perform actions during the OnDestroy() lifecycle of the application. Signature ```kotlin open fun onDestroy() ``` |
| **onPauseActivity** () | Called when the activity is in onPause callback. Override this method to perform actions during the OnPause() lifecycle of the application. Signature ```kotlin open fun onPauseActivity() ``` |
| **onResume** () | Called when the application is resumed. Override this method to perform actions during the OnResume() lifecycle of the application. Signature ```kotlin open fun onResume() ``` |
| **onSceneReady** () | Called when the scene is ready. Override this method to perform actions during the OnSceneReady() lifecycle of the application. Signature ```kotlin open fun onSceneReady() ``` |
| **onStart** () | Called when the application is started. Override this method to perform actions during the OnStart() lifecycle of the application. Signature ```kotlin open fun onStart() ``` |
| **onStopActivity** () | Called when the activity is in onStop callback. Be aware that onStop() is not guaranteed to be called. Override this method to perform actions during the OnStop() lifecycle of the application. Signature ```kotlin open fun onStopActivity() ``` |
| **onVRPause** () | Called when the VR mode is paused. Override this method to perform actions during the OnVRPause() lifecycle of the application. Signature ```kotlin open fun onVRPause() ``` |
| **onVRReady** () | Called when the VR mode is ready. Override this method to perform actions during the onVRReady() lifecycle of the application. Signature ```kotlin open fun onVRReady() ``` |
| **preRuntimeOnCreate** ( savedInstanceState ) | Called before the application's onCreate() method is called. Override this method to perform actions before the rest of the OnCreate() lifecycle of the application. Signature ```kotlin open fun preRuntimeOnCreate(savedInstanceState: Bundle?) ``` Parameters savedInstanceState: Bundle? The saved instance state of the application. |
| **registerRequiredOpenXRExtensions** () | Override this function to define a list of required OpenXR extensions that should be enabled by your application. Signature ```kotlin open fun registerRequiredOpenXRExtensions(): List<String> ``` Returns List A list of strings representing the required OpenXR extensions. |