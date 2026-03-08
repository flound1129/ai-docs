# NetworkedAssetLoader Object

Singleton for downloading and caching remote assets.

Manages the fetching of remote assets and caches them locally to avoid redundant downloads. Must be initialized with [NetworkedAssetLoader.init](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_networkedassetloader#init) before use.

Example usage:

```kotlin // Initialize the loader
NetworkedAssetLoader.init(File(applicationContext.getCacheDir().canonicalPath), OkHttpAssetFetcher())
// The ECS will use the networkedAssetLoader to download files that start with "http" and "https"
val modelUrl = Uri.parse("https://example.com/model.glb")
entity.setComponent(Mesh(modelUrl)) ```

## Signature

```kotlin
object NetworkedAssetLoader
```

## Properties

| **TAG** : String [Get] | Signature ```kotlin const val TAG: String ``` |
| --- | --- |

## Functions

| **destroy** () | Destroys the loader and cleans up any local files. Lifetime is managed by MeshManager. Signature ```kotlin fun destroy() ``` |
| --- | --- |
| **init** ( downloadDirectory , assetFetcher ) | Initializes the loader with a download directory and asset fetcher. Signature ```kotlin fun init(downloadDirectory: File, assetFetcher: AssetFetcher) ``` Parameters downloadDirectory: File Directory where downloaded assets will be stored assetFetcher: [AssetFetcher](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_assetfetcher) Implementation that handles the actual asset downloading |
| **requestAsset** ( url , extension ) | Requests an asset from a remote source. Downloads the asset if not already cached and returns a future with the local file path. The same asset will only be downloaded once, with subsequent requests returning the cached future. Signature ```kotlin fun requestAsset(url: Uri, extension: String): CompletableFuture<String> ``` Parameters url: Uri Remote location of the asset extension: String File extension to use for the downloaded file Returns CompletableFuture Future that resolves to the local file path when download completes |