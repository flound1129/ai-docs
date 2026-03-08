# SceneModel Enum

Defines the scene model versions used when loading scene data.

Scene models represent different versions of the spatial data format. When loading scene data from the device, you can specify which version to use based on your application's requirements.

## See Also

## Signature

```kotlin
enum SceneModel : Enum<SceneModel>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| V1 | Legacy scene model version |
| V2 | Current scene model version with improved features |
| V2_FALLBACK_V1 | Attempts to use V2, falls back to V1 if unavailable |