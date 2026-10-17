import numpy as np

class BaseMesh:
    def __init__(self):
        #open GL context
        self.ctx = None
        # shader program
        self.program = None
        #vertex buffer data type format "3f, 3f"
        self.vbo_format = None
        #Atrribute names. Forma: In posistion, in color
        self.attrs: tuple[str, ...] = None
        #vertex Array object
        self.vao = None

    def get_vertex_data(self) -> np.array: ...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        if vertex_data is None or len(vertex_data) == 0:
            return None
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attrs)], skip_errors=True
        )
        return vao

    def render(self):
        self.vao.render()

