# RecursiveFileObserver Class

*Modifiers:
final*

## Signature

```kotlin
class RecursiveFileObserver(path: File, onFileChanged: (String) -> Unit)
```

## Constructors

| **RecursiveFileObserver** ( path , onFileChanged ) | Signature ```kotlin constructor(path: File, onFileChanged: (String) -> Unit) ``` Parameters path: File onFileChanged: Function1 Returns [RecursiveFileObserver](/reference/spatial-sdk/v0.10.1/com_meta_spatial_debugtools_recursivefileobserver) |
| --- | --- |

## Functions

| **onEvent** ( event , filePath ) | Signature ```kotlin open fun onEvent(event: Int, filePath: String?) ``` Parameters event: Int filePath: String? |
| --- | --- |
| **startWatching** () | Signature ```kotlin open fun startWatching() ``` |
| **stopWatching** () | Signature ```kotlin open fun stopWatching() ``` |