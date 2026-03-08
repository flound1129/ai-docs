# AppSystemCommon Interface

This interface is used to provide a common interface for both AppSystemActivities and AppSystemServices. It provides access to the SystemManager and allows for registering mesh creators.

## Signature

```kotlin
interface AppSystemCommon
```

## Functions

| **getSystemManager** () | Signature ```kotlin abstract fun getSystemManager(): SystemManager ``` Returns [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) |
| --- | --- |
| **registerMeshCreator** ( baseUrl , creator ) | Registers a mesh creator for a base URL pattern. The creator will be invoked for any mesh URI that matches the base URL (scheme + authority + path). Query parameters from the full URI will be passed to the creator for customization. Example: ```kotlin // Register a creator for "mesh://custom/sphere" registerMeshCreator("mesh://custom/sphere") { entity, uri -> val radius = uri.getQueryParameter("radius")?.toFloatOrNull() ?: 1.0f val color = uri.getQueryParameter("color") ?: "white" createSphere(entity, radius, color) } // Later, use with parameters: Mesh(Uri.parse("mesh://custom/sphere?radius=2.5&color=red")) ``` Parameters baseUrl: String The base URL to match (e.g., "mesh://myapp/custom"). Query parameters are ignored in matching. creator: Function2 Function that takes an Entity and the full URI (including query params), returns a SceneMesh |
| **registerMeshCreator** ( meshURL , creator ) | Registers a simple mesh creator that doesn't need URI parameters. This is a convenience method for mesh creators that don't need to read query parameters from the URI. The mesh URL must match exactly. Example: ```kotlin registerMeshCreator("mesh://custom") { entity -> SceneMesh.box(-0.5f, -0.5f, -0.5f, 0.5f, 0.5f, 0.5f, material) } ``` Signature ```kotlin open fun registerMeshCreator(meshURL: String, creator: (entity: Entity) -> SceneMesh) ``` Parameters meshURL: String The exact mesh URL to match creator: Function1 Function that takes an Entity and returns a SceneMesh |
| **unregisterMeshCreator** ( baseUrl ) | Unregisters a mesh creator for the given base URL. Signature ```kotlin open fun unregisterMeshCreator(baseUrl: String) ``` Parameters baseUrl: String The base URL that was registered |