# MaterialSidedness Enum

Controls which sides of a mesh are rendered with a material.

Example usage:

```kotlin // Create a material that only renders the front side of polygons (default)
sceneMaterial.setSidedness(MaterialSidedness.FRONT_SIDED) ```

## Signature

```kotlin
enum MaterialSidedness : Enum<MaterialSidedness>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| FRONT_SIDED | Renders only the front side of polygons. Default option. |
| BACK_SIDED | Renders only the back side of polygons. |
| DOUBLE_SIDED | Renders both sides of polygons. |

## Properties

| **encoding** : Int [Get] | Integer value corresponding to the native graphics API encoding for this sidedness mode Signature ```kotlin val encoding: Int ``` |
| --- | --- |