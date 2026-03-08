# MeshCollision Enum

Mesh collision test type, used to determine how a mesh is hit tested. This is used in the [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) , [Panel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panel) , and [Hittable](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_hittable) components.

## Signature

```kotlin
enum MeshCollision : Enum<MeshCollision>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| NoCollision | no collision |
| LineTest | collisions occurs with linetests when visible |
| LineTest_IgnoreVisible | collisions occurs with linetests regardless of visible |