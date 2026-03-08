# TriangleMesh Class

*Modifiers:
final*

TriangleMesh provides direct access to the vertex and index data of a 3D mesh, allowing for dynamic creation and modification of geometry.

TriangleMesh can be used to create a SceneMesh via SceneMesh.fromTriangleMesh(), or to update an existing SceneMesh via SceneMesh.updateWithTriangleMesh().

Example usage:

```kotlin // Create a triangle mesh with 3 vertices and 3 indices (one triangle)
val mesh = TriangleMesh(
    numberVertices = 3,
    numberOfIndices = 3,
    materialRanges = intArrayOf(0, 3),  // All indices use the first material
    materials = arrayOf(material)
)
// Update the vertex positions, normals, and UVs
mesh.updateGeometry(
    startIndex = 0,
    positions = floatArrayOf(
        0f, 0f, 0f,    // Vertex 0
        1f, 0f, 0f,    // Vertex 1
        0f, 1f, 0f     // Vertex 2
    ),
    normals = floatArrayOf(
        0f, 0f, 1f,    // Normal for vertex 0
        0f, 0f, 1f,    // Normal for vertex 1
        0f, 0f, 1f     // Normal for vertex 2
    ),
    uvs = floatArrayOf(
        0f, 0f,        // UV for vertex 0
        1f, 0f,        // UV for vertex 1
        0f, 1f         // UV for vertex 2
    ),
    colors = null      // No per-vertex colors
)
// Update the triangle indices
mesh.updatePrimitives(
    startIndex = 0,
    indices = intArrayOf(0, 1, 2)  // Triangle connecting vertices 0, 1, and 2
)
// Convert to a SceneMesh for rendering
val sceneMesh = SceneMesh.fromTriangleMesh(mesh) ```

## Signature

```kotlin
class TriangleMesh
```

## Constructors

| **TriangleMesh** ( numberVertices , numberOfIndices , materialRanges , materials ) | Creates a new triangle mesh with the specified parameters. Signature ```kotlin constructor(numberVertices: Int, numberOfIndices: Int, materialRanges: IntArray, materials: Array<SceneMaterial>) ``` Parameters numberVertices: Int The number of vertices in the mesh numberOfIndices: Int The number of indices in the mesh materialRanges: IntArray Array specifying the range of indices that use each material. Format: start0, end0, start1, end1, ... where each pair defines the start (inclusive) and end (exclusive) indices for a material materials: Array Array of materials to use for the mesh Returns [TriangleMesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_trianglemesh) |
| --- | --- |

## Properties

| **handle** : Long [Get] | Signature ```kotlin var handle: Long ``` |
| --- | --- |
| **materials** : Array [Get] | Signature ```kotlin var materials: Array<SceneMaterial> ``` |

## Functions

| **destroy** () | Signature ```kotlin fun destroy() ``` |
| --- | --- |
| **updateGeometry** ( startIndex , positions , normals , uvs , colors ) | Updates the geometry data of the mesh. Signature ```kotlin fun updateGeometry(startIndex: Int, positions: FloatArray?, normals: FloatArray?, uvs: FloatArray?, colors: IntArray?) ``` Parameters startIndex: Int The index of the first vertex to update positions: FloatArray? Array of vertex positions as XYZ triplets x0, y0, z0, x1, y1, z1, ... normals: FloatArray? Array of vertex normals as XYZ triplets nx0, ny0, nz0, nx1, ny1, nz1, ... uvs: FloatArray? Array of texture coordinates as UV pairs u0, v0, u1, v1, ... colors: IntArray? Array of vertex colors as ARGB integers |
| **updatePrimitives** ( startIndex , indices ) | Updates the triangle indices of the mesh. Triangle indices define how vertices are connected to form triangles. Each triplet of indices represents one triangle. Signature ```kotlin fun updatePrimitives(startIndex: Int, indices: IntArray) ``` Parameters startIndex: Int The index of the first index to update indices: IntArray Array of vertex indices as triplets i0, i1, i2, i3, i4, i5, ... where each triplet (i0,i1,i2) defines one triangle |