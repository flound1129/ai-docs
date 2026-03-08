# ScenePhysicsObject Class

*Modifiers:
final*

`ScenePhysicsObject` has been moved from `com.meta.spatial.runtime` to `com.meta.spatial.physics` as part of decoupling physics from the core aether library.

```kotlin // OLD (no longer works)
import com.meta.spatial.runtime.ScenePhysicsObject
// NEW
import com.meta.spatial.physics.ScenePhysicsObject ```

```kotlin override fun registerFeatures(): List<SpatialFeature> {
    return listOf(
        PhysicsFeature(spatial),
        // ... other features
    )
} ```

```kotlin deps = [
    "//xplat/aether/libs/features/physics:physics",
] ```

Some physics methods have also moved from `SpatialInterface` to `PhysicsFeature` :

- `spatial.enablePhysicsDebugLines(enabled)` → `physicsFeature.enablePhysicsDebugLines(enabled)` - `spatial.setGravity(x, y, z)` → `physicsFeature.setGravity(x, y, z)`

Store a reference to your `PhysicsFeature` instance to access these methods.

## Signature

```kotlin
class ScenePhysicsObject
```