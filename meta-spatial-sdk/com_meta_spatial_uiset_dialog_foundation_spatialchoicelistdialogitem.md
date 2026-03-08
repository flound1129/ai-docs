# SpatialChoiceListDialogItem Class

*Modifiers:
final*

Represents an item in a spatial choice list dialog.

## Signature

```kotlin
data class SpatialChoiceListDialogItem(val leading: () -> Unit, val title: String, val subtitle: String, val enabled: Boolean = true)
```

## Constructors

| **SpatialChoiceListDialogItem** ( leading , title , subtitle , enabled ) | Signature ```kotlin constructor(leading: () -> Unit, title: String, subtitle: String, enabled: Boolean = true) ``` Parameters leading: Function0 A composable function that provides the leading content for the item. title: String The title text of the item. subtitle: String The subtitle text of the item. enabled: Boolean Indicates whether the item is enabled or not. Defaults to true. Returns [SpatialChoiceListDialogItem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_dialog_foundation_spatialchoicelistdialogitem) |
| --- | --- |

## Properties

| **enabled** : Boolean [Get] | Signature ```kotlin val enabled: Boolean = true ``` |
| --- | --- |
| **leading** : Function0 [Get] | Signature ```kotlin val leading: () -> Unit ``` |
| **subtitle** : String [Get] | Signature ```kotlin val subtitle: String ``` |
| **title** : String [Get] | Signature ```kotlin val title: String ``` |