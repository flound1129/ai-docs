# DataModelInspectorFeature Class

Implements
[SpatialFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature)
*Modifiers:
final*

The Data Model Inspector (DMI) feature provides real-time debugging capabilities for the ECS in a Spatial SDK project.

More info: [https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-tooling-dmi/](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-tooling-dmi/)

DMI offers a live view of your scene's data model directly in Android Studio, making debugging easier by allowing developers to:

- Monitor entity attributes in real-time as they change during runtime - Temporarily modify entity attributes without rebuilding the application - Select entities either from the inspector panel or directly in the 3D scene - Search and filter entities and their attributes

This feature works in conjunction with the Meta Horizon Android Studio Plugin, which provides a dedicated panel for interacting with the data model. This should not be enabled in the release version of an app.

```kotlin override fun registerFeatures(): List<SpatialFeature> {
  val features = mutableListOf<SpatialFeature>()
  if (BuildConfig.DEBUG) {
    ...
    features.add(DataModelInspectorFeature(spatial, this.componentManager))
  }
} ```

## See Also

- [SpatialFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature)

## Constructors

| **DataModelInspectorFeature** ( spatial , componentManager , port ) | Signature ```kotlin constructor(spatial: SpatialInterface, componentManager: ComponentManager, port: UShort) ``` Parameters spatial: [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) The SpatialInterface instance for the application componentManager: [ComponentManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentmanager) The ComponentManager instance of the application port: UShort The network port used for communication between the app and Android Studio plugin (default: 8011) Returns [DataModelInspectorFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_datamodelinspector_datamodelinspectorfeature) |
| --- | --- |

## Properties

| **componentManager** : [ComponentManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentmanager) [Get] | The ComponentManager instance of the application Signature ```kotlin val componentManager: ComponentManager ``` |
| --- | --- |
| **port** : UShort [Get] | The network port used for communication between the app and Android Studio plugin (default: 8011) Signature ```kotlin val port: UShort ``` |
| **spatial** : [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) [Get] | The SpatialInterface instance for the application Signature ```kotlin val spatial: SpatialInterface ``` |

## Functions

| **componentsToRegister** () | Override this function to define a list of components that should be used by the application. Signature ```kotlin open fun componentsToRegister(): List<ComponentRegistration> ``` Returns List A list of ComponentRegistration objects representing the components to register. |
| --- | --- |
| **earlySystemsToRegister** () | Override this method to register your systems that should be executed with [PriorityGroup](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_prioritygroup) EARLY. Signature ```kotlin open fun earlySystemsToRegister(): List<SystemBase> ``` Returns List A list of SystemBase objects |
| **getDependencies** () | Override this method to define a list of dependencies required by this feature. This will be verified at runtime. Example: ```kotlin // MyCustomFeature.kt override fun getDependencies(): List<KClass<out SpatialFeature>> { return listOf(ToolkitFeature::class) } @return A list of SpatialFeature classes representing the dependencies. ``` Signature ```kotlin open fun getDependencies(): List<KClass<out SpatialFeature>> ``` Returns List |
| **lateSystemsToRegister** () | Override this method to register your systems that should be executed with [PriorityGroup](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_prioritygroup) LATE. Signature ```kotlin open override fun lateSystemsToRegister(): List<SystemBase> ``` Returns List A list of SystemBase objects |
| **loadLibrary** ( libName ) | Loads a native library into the application. Signature ```kotlin open fun loadLibrary(libName: String) ``` Parameters libName: String The name of the library to load. |
| **onCreate** ( savedInstanceState ) | Called when the application is created. Override this method to perform actions during the OnCreate() lifecycle of the application. Signature ```kotlin open override fun onCreate(savedInstanceState: Bundle?) ``` Parameters savedInstanceState: Bundle? The saved instance state of the application. |
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