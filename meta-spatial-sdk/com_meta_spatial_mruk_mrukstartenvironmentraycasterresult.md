# MRUKStartEnvironmentRaycasterResult Enum

Result codes returned when attempting to start the environment raycaster. The environment raycaster enables raycasting against the scene mesh for collision detection and spatial queries.

## Signature

```kotlin
enum MRUKStartEnvironmentRaycasterResult : Enum<MRUKStartEnvironmentRaycasterResult>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| SUCCESS | The environment raycaster was successfully created and initialized. |
| ERROR | An error occurred while creating the environment raycaster. This may include initialization failures, resource allocation errors, or other internal errors not related to platform support. |
| UNSUPPORTED | Environment raycasting is not supported on this device or platform. |