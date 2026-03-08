# SpatialBasicDialog Function

*Modifiers:
final*

Displays a basic spatial dialog with a title, description, and action buttons.

## Signature

```kotlin
fun SpatialBasicDialog(title: String, description: String, primaryChoiceActionLabel: String, onPrimaryChoiceActionClick: () -> Unit, secondaryChoiceActionLabel: String? = null, onSecondaryChoiceActionClick: () -> Unit? = null, tertiaryChoiceActionLabel: String? = null, onTertiaryChoiceActionClick: () -> Unit? = null, leading: () -> Unit? = null, trailing: () -> Unit? = null, thumbnail: () -> Unit? = null, steps: SpatialDialogSteps? = null)
```

## Parameters

title:
String
The title of the dialog.
description:
String
The description of the dialog.
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
thumbnail:
Function0?
An optional composable to display as a thumbnail.
steps:
[SpatialDialogSteps?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_dialog_foundation_spatialdialogsteps)
An optional object representing the current step and total steps in the dialog.