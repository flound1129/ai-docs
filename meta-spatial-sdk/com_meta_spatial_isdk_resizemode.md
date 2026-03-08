# ResizeMode Enum

ResizeMode defines how a panel can be resized.

## Signature

```kotlin
enum ResizeMode : Enum<ResizeMode>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| Simple | Resize modifies entity scale component. |
| Relayout | Resize adjusts panel dimensions and re-renders UI. |
| None | Resize handles do nothing. Developers can write their own resize logic via InputListeners on the PanelSceneObject. |