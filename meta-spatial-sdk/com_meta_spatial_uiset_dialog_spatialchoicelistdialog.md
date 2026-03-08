# SpatialChoiceListDialog Function

*Modifiers:
final*

Displays a spatial dialog with a choice list, title, description, and action buttons.

## Signature

```kotlin
fun SpatialChoiceListDialog(title: String, description: String, listHeaderText: String, selectedItem: SpatialChoiceListDialogItem? = null, items: List<SpatialChoiceListDialogItem>, onItemSelected: (SpatialChoiceListDialogItem) -> Unit, primaryChoiceActionLabel: String, onPrimaryChoiceActionClick: () -> Unit, secondaryChoiceActionLabel: String? = null, onSecondaryChoiceActionClick: () -> Unit? = null, tertiaryChoiceActionLabel: String? = null, onTertiaryChoiceActionClick: () -> Unit? = null, leading: () -> Unit? = null, trailing: () -> Unit? = null)
```

## Parameters

title:
String
The title of the dialog.
description:
String
The description of the dialog.
listHeaderText:
String
The header text for the choice list.
selectedItem:
[SpatialChoiceListDialogItem?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_dialog_foundation_spatialchoicelistdialogitem)
The currently selected item in the choice list (optional).
items:
List
The list of items to display in the choice list.
onItemSelected:
Function1
The callback to invoke when an item is selected.
primaryChoiceActionLabel:
String
The label for the primary action button.
onPrimaryChoiceActionClick:
Function0
The callback to invoke when the primary action button is clicked.
secondaryChoiceActionLabel:
String?
The label for the secondary action button (optional).
onSecondaryChoiceActionClick:
Function0?
The callback to invoke when the secondary action button is clicked (optional).
tertiaryChoiceActionLabel:
String?
The label for the tertiary action button (optional).
onTertiaryChoiceActionClick:
Function0?
The callback to invoke when the tertiary action button is clicked (optional).
leading:
Function0?
An optional composable to display as leading content.
trailing:
Function0?
An optional composable to display as trailing content.