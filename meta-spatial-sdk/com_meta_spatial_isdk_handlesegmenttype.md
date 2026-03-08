# HandleSegmentType Enum

Enum matching the native HandleSegmentType in AetherHandleSegment.h Used to identify which handle segment was interacted with

Order: Clockwise from left (matches Android Rect order: left, top, right, bottom)

## Signature

```kotlin
enum HandleSegmentType : Enum<HandleSegmentType>
```

## Enumeration Constants

| Member |
| --- |
| FRONT_FACE_LEFT |
| FRONT_FACE_TOP |
| FRONT_FACE_RIGHT |
| FRONT_FACE_BOTTOM |
| CORNER_TOP_LEFT |
| CORNER_TOP_RIGHT |
| CORNER_BOTTOM_RIGHT |
| CORNER_BOTTOM_LEFT |
| RESIZE_CORNER_TOP_LEFT |
| RESIZE_CORNER_TOP_RIGHT |
| RESIZE_CORNER_BOTTOM_RIGHT |
| RESIZE_CORNER_BOTTOM_LEFT |

## Functions

| **getEdgeIndex** () | Get edge index (0-11) - now matches enum ordinal (clockwise from left) Signature ```kotlin fun getEdgeIndex(): Int ``` Returns Int |
| --- | --- |
| **isGrabCorner** () | Check if segment type is a corner (not resize) Signature ```kotlin fun isGrabCorner(): Boolean ``` Returns Boolean |
| **isGrabEdge** () | Check if segment type is an edge (top/bottom/left/right) Signature ```kotlin fun isGrabEdge(): Boolean ``` Returns Boolean |
| **isHorizontalEdge** () | Returns true for TOP and BOTTOM edges (horizontal orientation) Signature ```kotlin fun isHorizontalEdge(): Boolean ``` Returns Boolean |
| **isResizeCorner** () | Check if segment type is a resize corner Signature ```kotlin fun isResizeCorner(): Boolean ``` Returns Boolean |
| **isVerticalEdge** () | Returns true for LEFT and RIGHT edges (vertical orientation) Signature ```kotlin fun isVerticalEdge(): Boolean ``` Returns Boolean |

## Companion Object

### Companion Object Properties

| **grabCorners** : listOf(CORNER_TOP_LEFT, CORNER_TOP_RIGHT, CORNER_BOTTOM_LEFT, CORNER_BOTTOM_RIGHT) [Get] | Signature ```kotlin val grabCorners: listOf(CORNER_TOP_LEFT, CORNER_TOP_RIGHT, CORNER_BOTTOM_LEFT, CORNER_BOTTOM_RIGHT) ``` |
| --- | --- |
| **grabEdges** : listOf(FRONT_FACE_LEFT, FRONT_FACE_TOP, FRONT_FACE_RIGHT, FRONT_FACE_BOTTOM) [Get] | Signature ```kotlin val grabEdges: listOf(FRONT_FACE_LEFT, FRONT_FACE_TOP, FRONT_FACE_RIGHT, FRONT_FACE_BOTTOM) ``` |
| **resizeCorners** : listOf( RESIZE_CORNER_TOP_LEFT, RESIZE_CORNER_TOP_RIGHT, RESIZE_CORNER_BOTTOM_LEFT, RESIZE_CORNER_BOTTOM_RIGHT, ) [Get] | Signature ```kotlin val resizeCorners: listOf( RESIZE_CORNER_TOP_LEFT, RESIZE_CORNER_TOP_RIGHT, RESIZE_CORNER_BOTTOM_LEFT, RESIZE_CORNER_BOTTOM_RIGHT, ) ``` |