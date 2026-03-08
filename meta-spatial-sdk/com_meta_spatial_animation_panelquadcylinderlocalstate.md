# PanelQuadCylinderLocalState Class

*Modifiers:
final*

## Signature

```kotlin
data class PanelQuadCylinderLocalState(var type: PanelQuadCylinderAnimationType, val startTimeInMs: Long, val durationInMs: Long, var initialRadius: Float, var targetRadius: Float, var status: PanelQuadCylinderAnimationStatus, val isGrabbableEnabled: Boolean)
```

## Constructors

| **PanelQuadCylinderLocalState** ( type , startTimeInMs , durationInMs , initialRadius , targetRadius , status , isGrabbableEnabled ) | Signature ```kotlin constructor(type: PanelQuadCylinderAnimationType, startTimeInMs: Long, durationInMs: Long, initialRadius: Float, targetRadius: Float, status: PanelQuadCylinderAnimationStatus, isGrabbableEnabled: Boolean) ``` Parameters type: [PanelQuadCylinderAnimationType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_animation_panelquadcylinderanimationtype) startTimeInMs: Long durationInMs: Long initialRadius: Float targetRadius: Float status: [PanelQuadCylinderAnimationStatus](/reference/spatial-sdk/v0.10.1/com_meta_spatial_animation_panelquadcylinderanimationstatus) isGrabbableEnabled: Boolean Returns [PanelQuadCylinderLocalState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_animation_panelquadcylinderlocalstate) |
| --- | --- |

## Properties

| **durationInMs** : Long [Get] | Signature ```kotlin val durationInMs: Long ``` |
| --- | --- |
| **initialRadius** : Float [Get][Set] | Signature ```kotlin var initialRadius: Float ``` |
| **isGrabbableEnabled** : Boolean [Get] | Signature ```kotlin val isGrabbableEnabled: Boolean ``` |
| **startTimeInMs** : Long [Get] | Signature ```kotlin val startTimeInMs: Long ``` |
| **status** : [PanelQuadCylinderAnimationStatus](/reference/spatial-sdk/v0.10.1/com_meta_spatial_animation_panelquadcylinderanimationstatus) [Get][Set] | Signature ```kotlin var status: PanelQuadCylinderAnimationStatus ``` |
| **targetRadius** : Float [Get][Set] | Signature ```kotlin var targetRadius: Float ``` |
| **type** : [PanelQuadCylinderAnimationType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_animation_panelquadcylinderanimationtype) [Get][Set] | Signature ```kotlin var type: PanelQuadCylinderAnimationType ``` |