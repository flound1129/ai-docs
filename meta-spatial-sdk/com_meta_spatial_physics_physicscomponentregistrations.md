# PhysicsComponentRegistrations Object

Auto-generated component registrations for com.meta.spatial.physics.

Use [PhysicsComponentRegistrations.all](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_physicscomponentregistrations#all) to get all component registrations for use with [SpatialFeature.componentsToRegister](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature#componentstoregister) .

Example:

```kotlin override fun componentsToRegister(): List<ComponentRegistration> {
    return PhysicsComponentRegistrations.all()
} ```

## Signature

```kotlin
object PhysicsComponentRegistrations
```

## Functions

| **all** () | Returns all component registrations for this package. Signature ```kotlin fun all(): List<ComponentRegistration> ``` Returns List List of [ComponentRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentregistration) for all components in this package |
| --- | --- |