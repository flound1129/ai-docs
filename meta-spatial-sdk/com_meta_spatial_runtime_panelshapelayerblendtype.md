# PanelShapeLayerBlendType Enum

Defines the types of blends with an overlay.

When using layer config, these enums define the overall blending behavior, and based on this blend the panel will use a different combination of blending modes and shaders.

## Signature

```kotlin
enum PanelShapeLayerBlendType : Enum<PanelShapeLayerBlendType>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| OPAQUE | Opaque, writes color and depth for every pixel |
| MASKED | Uses alpha to coverage to ignore pixels with low alpha. For pixels that pass the alpha test, they write both color and depth. |
| ALPHA_BLEND | Applies alpha blending to the layer. This pass does not write depth, and can run into blending artifacts if multiple alpha layers are used, as well as transparent geometry objects. |