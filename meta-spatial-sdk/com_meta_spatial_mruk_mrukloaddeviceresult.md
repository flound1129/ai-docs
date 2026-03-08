# MRUKLoadDeviceResult Enum

Represents the possible results when loading spatial data from the device.

## See Also

- [MRUKFeature.loadSceneFromDevice](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukfeature#loadscenefromdevice)

## Signature

```kotlin
enum MRUKLoadDeviceResult : Enum<MRUKLoadDeviceResult>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| SUCCESS | Indicates the operation was successful. |
| ERROR_NO_ROOMS_FOUND | Indicates no rooms were found. The user has not completed space setup. |
| ERROR_INSUFFICIENT_RESOURCES | Indicates there were insufficient resources. Try again after a short delay. |
| ERROR_STORAGE_AT_CAPACITY | Indicates the storage capacity was reached during the operation. |
| ERROR_INSUFFICIENT_VIEW | Indicates the view was insufficient. The user needs to look around more for anchor tracking to work. |
| ERROR_PERMISSION_INSUFFICIENT | Indicates insufficient permissions for the operation. The user didn't give the permission for the app to load spatial data. |
| ERROR_RATE_LIMITED | Indicates the operation was rate limited. Try again after a short delay. |
| ERROR_TOO_DARK | Indicates the environment is too dark. |
| ERROR_TOO_BRIGHT | Indicates the environment is too bright. |
| ERROR_UNKNOWN | Indicates an unknown error occurred. |