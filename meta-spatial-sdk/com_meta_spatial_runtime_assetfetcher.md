# AssetFetcher Interface

## Signature

```kotlin
interface AssetFetcher
```

## Functions

| **fetchAsset** ( url , outFile , onSuccess , onError ) | Fetches the asset at the given url and downloads it to the given file path Signature ```kotlin abstract fun fetchAsset(url: Uri, outFile: File, onSuccess: () -> Unit, onError: (Exception) -> Unit) ``` Parameters url: Uri outFile: File onSuccess: Function0 onError: Function1 |
| --- | --- |