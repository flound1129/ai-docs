# ComponentRegistrations Object

Auto-generated component registrations for com.meta.spatial.mruk.

Use [ComponentRegistrations.all](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_componentregistrations#all) to get all component registrations for use with [SpatialFeature.componentsToRegister](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature#componentstoregister) .

Example:

```kotlin override fun componentsToRegister(): List<ComponentRegistration> {
    return ComponentRegistrations.all()
} ```

## Signature

```kotlin
object ComponentRegistrations
```

## Functions

| **all** () | Returns all component registrations for this package. Signature ```kotlin fun all(): List<ComponentRegistration> ``` Returns List List of [ComponentRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentregistration) for all components in this package |
| --- | --- |