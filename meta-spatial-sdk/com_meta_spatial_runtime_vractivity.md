# VrActivity Class

*Modifiers:
open*

VrActivity serves as the base class inherited by AppSystemActivity, which should be used for creating Spatial Activities instead of directly subclassing VrActivity. This class provides essential functionalities required by all Meta Spatial applications, including:

- Lifecycle management: Handles Android lifecycle events. - Input management: Manages user inputs within the virtual environment. - Scene management: Oversees the creation and updating of scenes, helping to organize content and manage rendering. - DataModel setup: Prepares and manages the data models necessary for application functionality.

As a subclass of Android's Activity, VrActivity includes all standard Android lifecycle callbacks, such as onCreate().

## Signature

```kotlin
open class VrActivity
```

## Constructors

| **VrActivity** () | Signature ```kotlin constructor() ``` Returns [VrActivity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_vractivity) |
| --- | --- |

## Properties

| **componentManager** : [ComponentManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentmanager) [Get] | Signature ```kotlin val componentManager: ComponentManager ``` |
| --- | --- |
| **scene** : [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) [Get] | Signature ```kotlin val scene: Scene ``` |
| **spatialContext** : [SpatialContext](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialcontext) [Get] | Signature ```kotlin val spatialContext: SpatialContext ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get] | Signature ```kotlin val systemManager: SystemManager ``` |

## Functions

| **audioPauseMode** () | Controls when audio is automatically paused and resumed. Override this method to change the audio pause behavior: - [AudioPauseMode.ACTIVITY_FOCUS](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_audiopausemode#activity_focus) (default): Audio pauses on Android Activity onPause/onResume - [AudioPauseMode.OPENXR_FOCUS](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_audiopausemode#openxr_focus) : Audio pauses based on OpenXR session focus state - [AudioPauseMode.MANUAL](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_audiopausemode#manual) : Audio is not automatically paused; developer controls via [Scene.setAudioEnabled](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene#setaudioenabled) Example: ```kotlin override fun audioPauseMode(): AudioPauseMode = AudioPauseMode.OPENXR_FOCUS ``` Signature ```kotlin open fun audioPauseMode(): AudioPauseMode ``` Returns [AudioPauseMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_audiopausemode) |
| --- | --- |
| **dispatchGenericMotionEvent** ( event ) | Dispatches a generic motion event to the appropriate game controller. Signature ```kotlin open fun dispatchGenericMotionEvent(event: MotionEvent): Boolean ``` Parameters event: MotionEvent The motion event to dispatch. Returns Boolean True if the event was handled, false otherwise. |
| **dispatchKeyEvent** ( event ) | Dispatches a key event to the appropriate game controller. Signature ```kotlin open fun dispatchKeyEvent(event: KeyEvent): Boolean ``` Parameters event: KeyEvent The key event to dispatch. Returns Boolean True if the event was handled, false otherwise. |
| **doFrame** ( frameTimeNanos ) | Called when a new display frame is being rendered. Signature ```kotlin open fun doFrame(frameTimeNanos: Long) ``` Parameters frameTimeNanos: Long |
| **findFeature** ( clazz ) | Signature ```kotlin fun <T : SpatialFeature> findFeature(clazz: KClass<T>): T ``` Parameters clazz: KClass Returns [VrActivity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_vractivity) |
| **findFeature** () | Signature ```kotlin inline fun <T : SpatialFeature> findFeature(): T ``` Returns [VrActivity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_vractivity) |
| **getComponentManager** () | Returns the singleton component manager for the application. Signature ```kotlin fun getComponentManager(): ComponentManager ``` Returns [ComponentManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentmanager) The component manager for the application. |
| **getDataModel** () | Returns the singleton DataModel for the application. Signature ```kotlin fun getDataModel(): DataModel ``` Returns [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The data model for the application. |
| **getGameControllerDeviceIds** () | Returns a set of device IDs for all connected game controllers. Signature ```kotlin fun getGameControllerDeviceIds(): Set<Int> ``` Returns Set A set of device IDs for all connected game controllers. |
| **getSceneObject** () | Returns the singleton scene object for the application. Signature ```kotlin fun getSceneObject(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene object for the application. |
| **getSystemManager** () | Returns the singleton system manager for the application. Signature ```kotlin fun getSystemManager(): SystemManager ``` Returns [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager for the application. |
| **internalOnSessionStateChanged** ( stateValue ) | Internal JNI callback that receives the session state as an integer from C++. This method converts the integer to a SessionState enum and calls the public callback. Applications should not override this method. Signature ```kotlin open fun internalOnSessionStateChanged(stateValue: Int) ``` Parameters stateValue: Int The session state as an integer (0-8) |
| **loadLibrary** ( name ) | Loads a native C++ library. This method should be called in onCreate(). Signature ```kotlin open fun loadLibrary(name: String) ``` Parameters name: String The name of the library without the filename extensions. |
| **onCreate** ( savedInstanceState ) | Called when the VRActivity is first created. This method creates the necessary building blocks for a Spatial application. It initializes the VrActivity, including loading the Meta Spatial SDK library, registering game controller management, creating a new spatial instance, and initializing the SpatialFeature manager. Signature ```kotlin open fun onCreate(savedInstanceState: Bundle?) ``` Parameters savedInstanceState: Bundle? If the activity is being re-initialized after previously being shut down then this Bundle contains the data it most recently supplied in onSaveInstanceState(Bundle). Note: Otherwise it is null. |
| **onDestroy** () | Called when the app is destroyed. VrActivity::onDestroy will clean up all the resources and trigger garbage collection. If you override this method, be sure to call super.onDestroy(). Signature ```kotlin open fun onDestroy() ``` |
| **onHMDMounted** () | Signature ```kotlin open fun onHMDMounted() ``` |
| **onHMDUnmounted** () | Signature ```kotlin open fun onHMDUnmounted() ``` |
| **onPause** () | Called as part of the activity lifecycle when an activity is going into the background, but has not yet been killed. The counterpart to onResume(). If you override this method, be sure to call super.onPause(). Signature ```kotlin open fun onPause() ``` |
| **onPostResume** () | Called after activity resume is complete. If you override this method, be sure to call super.onPostResume(). Signature ```kotlin open fun onPostResume() ``` |
| **onRecenter** ( isUserInitiated ) | This hook is called when the VRActivity is recentered. Signature ```kotlin open fun onRecenter(isUserInitiated: Boolean) ``` Parameters isUserInitiated: Boolean |
| **onResume** () | Called when the activity will start interacting with the user. If you override this method, be sure to call super.onResume() Signature ```kotlin open fun onResume() ``` |
| **onSceneReady** () | This hook is called on the first onResume(), after the scene is loaded in onCreate(). It will invoke all the onSceneReady() hooks of the registered SpatialFeatures. Signature ```kotlin open fun onSceneReady() ``` |
| **onSceneTick** () | Called every tick in the application to update the scene. Signature ```kotlin open fun onSceneTick() ``` |
| **onSessionStateChanged** ( state ) | Called when the OpenXR session state changes. This callback is invoked whenever the XR runtime transitions between different session states. Applications can override this method to respond to state changes, such as preparing resources when the session becomes ready, or pausing rendering when losing focus. Signature ```kotlin open fun onSessionStateChanged(state: SessionState) ``` Parameters state: [SessionState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sessionstate) The new session state |
| **onSpatialShutdown** () | Called when the VRActivity is shutting down. This method will invoke all the onSpatialShutdown() callbacks of the registered SpatialFeatures. Signature ```kotlin open fun onSpatialShutdown() ``` |
| **onStart** () | Called when the activity is becoming visible to the user. If you override this method, be sure to call super.onStart(). Signature ```kotlin open fun onStart() ``` |
| **onStop** () | Called when the app is no longer visible to the user. You will next receive either onRestart(), onDestroy(), or nothing, depending on later user activity. If you override this method, be sure to call super.onStop(). Signature ```kotlin open fun onStop() ``` |
| **onVRPause** () | This hook is called when the VRActivity switches from immersive to non-immersive mode. It will invoke all the onVRPause() hooks of the registered SpatialFeatures. Signature ```kotlin open fun onVRPause() ``` |
| **onVRReady** () | This hook is called when the immersive Spatial application is first loaded or is changed from 2D mode to immersive (VR) mode. It will invoke all the onVRReady() hooks of the registered SpatialFeatures. Signature ```kotlin open fun onVRReady() ``` |
| **pinGameController** ( deviceId , func ) | Pins a game controller with the given device ID and associates it with the given function. Parameters deviceId: Int The device ID of the game controller to pin. func: Function2 The function to associate with the game controller. |
| **registerFeatures** () | Override this method to register your own SpatialFeatures. This is called in onCreate(). Signature ```kotlin open fun registerFeatures(): List<SpatialFeature> ``` Returns List |
| **registerRequiredOpenXRExtensions** () | Signature ```kotlin open fun registerRequiredOpenXRExtensions(): List<String> ``` Returns List |
| **registerSystemFeatures** () | Signature ```kotlin open fun registerSystemFeatures(): List<SpatialFeature> ``` Returns List |
| **renderConfiguration** () | Controls the render resolution scaling for VR applications. This configuration allows adjusting the resolution at which VR content is rendered, which affects both visual quality and performance. Signature ```kotlin open fun renderConfiguration(): RenderConfiguration ``` Returns [RenderConfiguration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_renderconfiguration) |
| **runOnMainThread** ( runnable ) | This method provides a way to run a Runnable on the activity's main thread. Signature ```kotlin fun runOnMainThread(runnable: Runnable) ``` Parameters runnable: Runnable |
| **setBaseHref** ( baseHref ) | Sets the base href for the application. Signature ```kotlin open fun setBaseHref(baseHref: String) ``` Parameters baseHref: String The new base href for the application. |
| **tryFindFeature** ( clazz ) | Signature ```kotlin fun <T : SpatialFeature> tryFindFeature(clazz: KClass<T>): T? ``` Parameters clazz: KClass Returns [VrActivity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_vractivity) |
| **tryFindFeature** () | Signature ```kotlin inline fun <T : SpatialFeature> tryFindFeature(): T? ``` Returns [VrActivity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_vractivity) |
| **unpinGameController** ( deviceId ) | Unpins a game controller with the given device ID. Signature ```kotlin fun unpinGameController(deviceId: Int) ``` Parameters deviceId: Int The device ID of the game controller to unpin. |
| **useVolumes** () | Signature ```kotlin open fun useVolumes(): Boolean ``` Returns Boolean |