# SortOrder Enum

Defines the rendering order for materials in a 3D scene.

Order is defined as:

- PreProcess - Opaque - Masked - HolePunch - Translucent - PostProcess

Example usage:

```kotlin // Set a material to render during the translucent pass
material.setSortOrder(SortOrder.TRANSLUCENT) ```

## Signature

```kotlin
enum SortOrder : Enum<SortOrder>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| OPAQUE | For fully opaque materials that don't require alpha blending. Rendered front-to-back for efficiency with depth testing. |
| MASKED | For materials with binary transparency (fully opaque or fully transparent pixels). No rendering order applied based on distance. |
| TRANSLUCENT | For materials with partial transparency that require alpha blending. Rendered back-to-front to ensure correct blending. |
| POSTPROCESS | For effects that are applied at the end of the rendering pipeline. No rendering order applied based on distance. |
| PREPROCESS | For effects that need to be applied at the beginning of the rendering pipeline. Rendered front-to-back. Rendered before all other objects (first in the rendering sequence). |
| HOLE_PUNCH | For materials that "punch holes" in the scene, typically used with layers. Rendered front-to-back. |

## Properties

| **order** : Int [Get] | The numeric value representing the SortOrder type. Signature ```kotlin val order: Int ``` |
| --- | --- |