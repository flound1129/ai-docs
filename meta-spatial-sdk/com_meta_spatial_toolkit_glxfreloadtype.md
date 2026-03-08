# GLXFReloadType Enum

GLXFReloadType is an enum that specifies how GLXFs should be reloaded.

KEEP_EXISTING_ENTITIES: Keeps existing entities and updates them with new data from the reloaded GLXF file.

DELETE_AND_RECREATE_ENTITIES: Deletes existing entities and recreates them with new data from the reloaded GLXF file.

The default value of a GLXFManager is DELETE_AND_RECREATE_ENTITIES.

## Signature

```kotlin
enum GLXFReloadType : Enum<GLXFReloadType>
```

## Enumeration Constants

| Member |
| --- |
| KEEP_EXISTING_ENTITIES |
| DELETE_AND_RECREATE_ENTITIES |