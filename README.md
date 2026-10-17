# Voxel Engine

A 3D Voxel Engine implemented in Python with **Pygame**, **ModernGL** (OpenGL 3.3 Core Profile), **PyGLM**, and JIT-accelerated mesh generation using **Numba** and **NumPy**.

---

## 🚀 Features

- **ModernGL & OpenGL 3.3 Core**: High-performance hardware-accelerated rendering with custom vertex and fragment shaders.
- **Numba JIT Mesh Generation**: Fast chunk meshing (`chunk_mesh_builder.py`) using Numba's `@njit` compilation for high framerates.
- **Chunk Management**: 3D infinite/expandable chunk-based terrain structure (`32x32x32` voxel chunk volumes).
- **Voxel Raycasting & Interaction**: Custom voxel raycasting with face detection for placing and removing blocks.
- **First-Person Camera**: Smooth 6-DOF camera controls with yaw/pitch clamping, mouse capture, and keyboard navigation.
- **Custom Shaders & Texturing**: Mipmapped texture filtering, nearest-neighbor sampling for pixel art aesthetics, and OpenGL depth testing with face culling.

---

## 🎮 Controls

| Action | Control |
|---|---|
| **Move Forward / Backward** | `W` / `S` |
| **Strafe Left / Right** | `A` / `D` |
| **Move Up / Down** | `Q` / `E` |
| **Look / Aim** | `Mouse Movement` |
| **Interact / Place / Break** | `Left Click` / `Right Click` |
| **Exit / Release Mouse** | `ESC` |

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cRodriguez6/voxel-engine.git
   cd voxel-engine
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the engine:**
   ```bash
   python3 main.py
   ```

---

## 📂 Project Structure

```text
├── assets/                  # Textures and sprites
├── meshes/                  # Mesh builders and OpenGL buffers
│   ├── base_mesh.py         # Base VAO / VBO abstractions
│   ├── chunk_mesh.py        # Chunk mesh representation
│   ├── chunk_mesh_builder.py# Numba-accelerated greedy/culled face mesher
│   └── quad_mesh.py         # 2D / Quad primitives
├── shaders/                 # GLSL Vertex & Fragment shaders
│   ├── chunk.vert           # Chunk vertex shader
│   ├── chunk.frag           # Chunk fragment shader
│   ├── quad.vert            # Quad vertex shader
│   └── quad.frag            # Quad fragment shader
├── world_objects/           # World objects and chunk instances
│   └── chunk.py             # Chunk data representation
├── camera.py                # 3D Camera with view and projection matrices
├── main.py                  # Engine entrypoint and loop
├── player.py                # Player movement, inputs, and controls
├── scene.py                 # Scene composition and render pipeline
├── settings.py              # Configuration constants and window parameters
├── shader_program.py        # Shader loading and uniform management
├── textures.py              # Texture loader and sampler settings
├── voxel_handler.py         # Voxel raycasting, add/delete handlers
└── world.py                 # Chunk generation and world orchestration
```
