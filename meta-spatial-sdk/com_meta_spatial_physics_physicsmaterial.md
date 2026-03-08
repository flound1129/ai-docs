# PhysicsMaterial Enum

Allows you to apply properties of certain materials to your physics objects. These are loosely researched values, and are not guaranteed to be accurate. Please use at your own risk

## Signature

```kotlin
enum PhysicsMaterial : Enum<PhysicsMaterial>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| WOOD | Accuracy is based on the following references. Density from: [https://www.britannica.com/science/wood-plant-tissue/Properties-of-wood](https://www.britannica.com/science/wood-plant-tissue/Properties-of-wood) Restitution from: [https://www.researchgate.net/figure/Particle-particle-coefficient-of-restitution-e-p-for-wood-pellet-particles-as-a_fig3_347357507](https://www.researchgate.net/figure/Particle-particle-coefficient-of-restitution-e-p-for-wood-pellet-particles-as-a_fig3_347357507) Friction from: [https://www.researchgate.net/publication/3185930_A_Comprehensive_Friction_Data](https://www.researchgate.net/publication/3185930_A_Comprehensive_Friction_Data) |
| LEAD | Accuracy is based on the following references. Density from: [https://physics.nist.gov/cgi-bin/Star/compos.pl?mode=text & matno=082](https://physics.nist.gov/cgi-bin/Star/compos.pl?mode=text&matno=082) Friction from: [https://www.engineersedge.com/coeffients_of_friction.htm](https://www.engineersedge.com/coeffients_of_friction.htm) |

## Properties

| **density** : Float [Get] | Signature ```kotlin val density: Float ``` |
| --- | --- |
| **friction** : [FrictionObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_frictionobject) [Get] | Signature ```kotlin val friction: FrictionObject ``` |
| **restitution** : Float [Get] | Signature ```kotlin val restitution: Float ``` |