# AppSystemService Class

Extends
VrService
Implements
[AppSystemCommon](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_appsystemcommon)
, SpatialViewModelOwner
*Modifiers:
open*

AppSystemService serves as the base class for all Spatial SDK services. It contains all Android service lifecycle callbacks: onCreate, onDestroy, and others. It also provides scene lifecycle callbacks: onSceneReady and onSceneTick. This class also provides hooks to override system features through registerSystemFeatures and to register panels through registerPanels.

## Signature

```kotlin
open class AppSystemService : VrService, AppSystemCommon, SpatialViewModelOwner
```

## Constructors

| **AppSystemService** () | Signature ```kotlin constructor() ``` Returns [AppSystemService](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_appsystemservice) |
| --- | --- |

## Properties

| **componentManager** : [ComponentManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentmanager) [Get] | Signature ```kotlin val componentManager: ComponentManager ``` |
| --- | --- |
| **glXFManager** : [GLXFManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfmanager) [Get] | Signature ```kotlin val glXFManager: GLXFManager ``` |
| **panelRegistrations** : HashMap<Int, PanelRegistration> [Get] | Signature ```kotlin val panelRegistrations: HashMap<Int, PanelRegistration> ``` |
| **registeredReceivers** : List [Get][Set] | Signature ```kotlin var registeredReceivers: List ``` |
| **scene** : [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) [Get] | Signature ```kotlin val scene: Scene ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get] | Signature ```kotlin val systemManager: SystemManager ``` |
| **viewModels** : MutableSet [Get] | Signature ```kotlin open override val viewModels: MutableSet<SpatialViewModel> ``` |

## Functions

| **doFrame** ( frameTimeNanos ) | Signature ```kotlin open fun doFrame(frameTimeNanos: Long) ``` Parameters frameTimeNanos: Long |
| --- | --- |
| **findFeature** ( clazz ) | Signature ```kotlin fun <T : SpatialFeature> findFeature(clazz: KClass<T>): T ``` Parameters clazz: KClass Returns VrService |
| **findFeature** () | Signature ```kotlin inline fun <T : SpatialFeature> findFeature(): T ``` Returns VrService |
| **getComponentManager** () | Signature ```kotlin fun getComponentManager(): ComponentManager ``` Returns [ComponentManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentmanager) |
| **getDataModel** () | Signature ```kotlin fun getDataModel(): DataModel ``` Returns [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) |
| **getSceneObject** () | Signature ```kotlin fun getSceneObject(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) |
| **getSystemManager** () | Signature ```kotlin fun getSystemManager(): SystemManager ``` Returns [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) |
| **onBind** ( intent ) | Signature ```kotlin open fun onBind(intent: Intent): IBinder ``` Parameters intent: Intent Returns IBinder |
| **onCreate** () | Called when the service is first created. Override this lifecycle callback method to do all of your normal static set up: creating views, setting the content view, register Components as well as Systems and etc. You can also perform dynamic setup, such as querying for data and loading it into the view. This will also be called for all activities that are restored to their state when last paused or stopped. If you override this method, be sure to call super.onCreate(). Signature ```kotlin open override fun onCreate() ``` |
| **onDestroy** () | Called when the service is destroyed. Override this method to perform any final cleanup. If you override this method, be sure to call super.onDestroy() Note: This is not guaranteed to be called, as the OS may kill the service's hosting process at any time. Signature ```kotlin open override fun onDestroy() ``` |
| **onHMDMounted** () | Signature ```kotlin open fun onHMDMounted() ``` |
| **onHMDUnmounted** () | Signature ```kotlin open fun onHMDUnmounted() ``` |
| **onRebind** ( intent ) | Signature ```kotlin open fun onRebind(intent: Intent) ``` Parameters intent: Intent |
| **onRecenter** ( isUserInitiated ) | Signature ```kotlin open fun onRecenter(isUserInitiated: Boolean) ``` Parameters isUserInitiated: Boolean |
| **onSceneReady** () | This hook is called on the first onResume(), after the scene is loaded in onCreate(). This is where you should call the scene APIs such as setReferenceSpace to define your scene. If you override this method, be sure to call super.onSceneReady(). Signature ```kotlin open override fun onSceneReady() ``` |
| **onSceneTick** () | Called every tick in the application. It is advisable to use this lifecycle callback method sparingly and to create Systems that manage logic in every tick. If you override this method, be sure to call super.onSceneTick(). Signature ```kotlin open override fun onSceneTick() ``` |
| **onSessionStateChanged** ( state ) | Called when the OpenXR session state changes. This callback is invoked whenever the XR runtime transitions between different session states. Applications can override this method to respond to state changes, such as preparing resources when the session becomes ready, or pausing rendering when losing focus. Signature ```kotlin open fun onSessionStateChanged(state: SessionState) ``` Parameters state: [SessionState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sessionstate) The new session state |
| **onStartCommand** ( intent , flags , startId ) | Signature ```kotlin open fun onStartCommand(intent: Intent, flags: Int, startId: Int): Int ``` Parameters intent: Intent flags: Int startId: Int Returns Int |
| **onUnbind** ( intent ) | Signature ```kotlin open fun onUnbind(intent: Intent): Boolean ``` Parameters intent: Intent Returns Boolean |
| **onVRPause** () | Signature ```kotlin open fun onVRPause() ``` |
| **onVRReady** () | Signature ```kotlin open fun onVRReady() ``` |
| **registerFeatures** () | Signature ```kotlin open fun registerFeatures(): List<SpatialFeature> ``` Returns List |
| **registerMeshCreator** ( baseUrl , creator ) | Registers a mesh creator for a base URL pattern. The creator will be invoked for any mesh URI that matches the base URL (scheme + authority + path). Query parameters from the full URI will be passed to the creator for customization. Example: ```kotlin // Register a creator for "mesh://custom/sphere" registerMeshCreator("mesh://custom/sphere") { entity, uri -> val radius = uri.getQueryParameter("radius")?.toFloatOrNull() ?: 1.0f val color = uri.getQueryParameter("color") ?: "white" createSphere(entity, radius, color) } // Later, use with parameters: Mesh(Uri.parse("mesh://custom/sphere?radius=2.5&color=red")) ``` Parameters baseUrl: String The base URL to match (e.g., "mesh://myapp/custom"). Query parameters are ignored in matching. creator: Function2 Function that takes an Entity and the full URI (including query params), returns a SceneMesh |
| **registerMeshCreator** ( meshURL , creator ) | Registers a simple mesh creator that doesn't need URI parameters. This is a convenience method for mesh creators that don't need to read query parameters from the URI. The mesh URL must match exactly. Example: ```kotlin registerMeshCreator("mesh://custom") { entity -> SceneMesh.box(-0.5f, -0.5f, -0.5f, 0.5f, 0.5f, 0.5f, material) } ``` Signature ```kotlin open fun registerMeshCreator(meshURL: String, creator: (entity: Entity) -> SceneMesh) ``` Parameters meshURL: String The exact mesh URL to match creator: Function1 Function that takes an Entity and returns a SceneMesh |
| **registerPanel** ( panelRegistration ) | This is used to register a panel. This is called within the onCreate lifecycle for every PanelRegistration returned by registerPanels. It is strongly discouraged to call this directly to dynamically register panels, as panels should be registered during OnCreate() Signature ```kotlin fun registerPanel(panelRegistration: PanelRegistration) ``` Parameters panelRegistration: [PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration) |
| **registerPanels** () | This hook is where you should register your panels. This is called within the onCreate lifecycle. Signature ```kotlin open fun registerPanels(): List<PanelRegistration> ``` Returns List |
| **registerSystemFeatures** () | This hook is where the application registers SystemFeatures such as ToolkitFeature. This is called within the onCreate lifecycle. Note that to register a custom SpatialFeature, override registerFeatures instead. Signature ```kotlin open override fun registerSystemFeatures(): List<SpatialFeature> ``` Returns List |
| **runOnMainThread** ( runnable ) | Signature ```kotlin fun runOnMainThread(runnable: Runnable) ``` Parameters runnable: Runnable |
| **setBaseHref** ( baseHref ) | Signature ```kotlin open fun setBaseHref(baseHref: String) ``` Parameters baseHref: String |
| **tryFindFeature** ( clazz ) | Signature ```kotlin fun <T : SpatialFeature> tryFindFeature(clazz: KClass<T>): T? ``` Parameters clazz: KClass Returns VrService? |
| **tryFindFeature** () | Signature ```kotlin inline fun <T : SpatialFeature> tryFindFeature(): T? ``` Returns VrService? |
| **unregisterMeshCreator** ( baseUrl ) | Unregisters a mesh creator for the given base URL. Signature ```kotlin open fun unregisterMeshCreator(baseUrl: String) ``` Parameters baseUrl: String The base URL that was registered |