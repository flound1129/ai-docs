# MRUKLabel Enum

Defines the different types of spatial objects and surfaces that can be detected and labeled in a mixed reality environment.

## Signature

```kotlin
enum MRUKLabel : Enum<MRUKLabel>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| FLOOR | A floor surface in the room |
| CEILING | A ceiling surface in the room |
| WALL_FACE | A wall surface in the room |
| TABLE | A table or desk surface |
| COUCH | A couch or sofa |
| DOOR_FRAME | A door frame opening |
| WINDOW_FRAME | A window frame opening |
| OTHER | An unclassified object |
| STORAGE | A storage unit such as a shelf or cabinet |
| BED | A bed |
| SCREEN | A screen such as a TV or monitor |
| LAMP | A lamp or light fixture |
| PLANT | A plant |
| WALL_ART | Wall art such as a painting or poster |
| GLOBAL_MESH | The global mesh representing the entire room geometry |
| INVISIBLE_WALL_FACE | An invisible wall face used for boundary detection |
| UNKNOWN | An unknown or unrecognized label type |
| INNER_WALL_FACE | An inner wall face within a room subdivision |
| INNER_TABLETOP | The top surface of a table |
| INNER_SITTING_AREA | A sitting area on furniture such as a couch |
| INNER_SLEEPING_AREA | A sleeping area on a bed |
| INNER_STORAGE_TOP | The top surface of a storage unit |