# PanelDisplayBase Class

*Modifiers:
open*

Handles displaying content on panels. Supports two display methods:

- Using VirtualDisplay with Presentation for custom views - Launching an Activity via an intent to populate the panel

## Constructors

| **PanelDisplayBase** ( ctx , panelSurface , surfaceDPI , getView , intent , themeResourceId , onAutoReleased , initializeInfra ) | Parameters ctx: Context The context in which the display operates. panelSurface: [PanelSurface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelsurface) The surface on which the panel is displayed. surfaceDPI: Int The DPI of the surface. getView: Function1? A lambda function to get the view to be displayed, if any. intent: Intent? The intent used to start an activity, if applicable. themeResourceId: Int The resource ID for the theme to be applied to the presentation. onAutoReleased: Function0? A callback function to be invoked when Activity panels are auto-released. initializeInfra: Boolean Returns [PanelDisplayBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_paneldisplaybase) |
| --- | --- |

## Properties

| **heightInPx** : Int [Get] | Signature ```kotlin var heightInPx: Int ``` |
| --- | --- |
| **panelSurface** : [PanelSurface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelsurface) [Get][Set] | The surface on which the panel is displayed. Signature ```kotlin var panelSurface: PanelSurface ``` |
| **rootView** : View? [Get] | Signature ```kotlin var rootView: View ``` |
| **surfaceDPI** : Int [Get][Set] | The DPI of the surface. Signature ```kotlin var surfaceDPI: Int ``` |
| **widthInPx** : Int [Get] | Signature ```kotlin var widthInPx: Int ``` |

## Functions

| **destroy** () | Signature ```kotlin open fun destroy() ``` |
| --- | --- |
| **dispatchEvent** ( motionEvent , isGenericEvent ) | Dispatches input events to the appropriate target Signature ```kotlin open fun dispatchEvent(motionEvent: MotionEvent, isGenericEvent: Boolean) ``` Parameters motionEvent: MotionEvent The motion event to dispatch isGenericEvent: Boolean Whether this is a generic motion event (hover) or touch event |
| **resize** ( newPanelSurface , newWidthInPx , newHeightInPx , dpi ) | Resizes the display to the specified dimensions in pixels. This will update the task container and virtual display with the new surface. Signature ```kotlin open fun resize(newPanelSurface: PanelSurface, newWidthInPx: Int, newHeightInPx: Int, dpi: Int) ``` Parameters newPanelSurface: [PanelSurface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelsurface) newWidthInPx: Int The new width in pixels newHeightInPx: Int The new height in pixels dpi: Int The DPI for the new surface |