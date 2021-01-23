from glnext_compiler import glsl


def test_compile_compute_shader():
    shader = glsl('''
        #version 450
        #pragma shader_stage(compute)

        layout (binding = 0) buffer StorageBuffer {
            float number[];
        };

        layout (binding = 1) buffer Output {
            float result[];
        };

        void main() {
            result[gl_GlobalInvocationID.x] = number[gl_GlobalInvocationID.x] * 2.0 + 1.0;
        }
    ''')

    assert type(shader) is bytes
    assert shader[:4].hex() == '03022307'
    assert len(shader) % 4 == 0


def test_compile_vertex_shader():
    shader = glsl('''
        #version 450
        #pragma shader_stage(vertex)

        layout (location = 0) out vec4 out_color;

        vec2 positions[3] = vec2[](
            vec2(-0.5, -0.5),
            vec2(0.5, -0.5),
            vec2(0.0, 0.5)
        );

        vec4 colors[3] = vec4[](
            vec4(1.0, 0.0, 0.0, 1.0),
            vec4(0.0, 1.0, 0.0, 1.0),
            vec4(0.0, 0.0, 1.0, 1.0)
        );

        void main() {
            gl_Position = vec4(positions[gl_VertexIndex], 0.0, 1.0);
            out_color = colors[gl_VertexIndex];
        }
    ''')

    assert type(shader) is bytes
    assert shader[:4].hex() == '03022307'
    assert len(shader) % 4 == 0


def test_compile_fragment_shader():
    shader = glsl('''
        #version 450
        #pragma shader_stage(fragment)

        layout (location = 0) in vec4 in_color;
        layout (location = 0) out vec4 out_color;

        void main() {
            out_color = in_color;
        }
    ''')

    assert type(shader) is bytes
    assert shader[:4].hex() == '03022307'
    assert len(shader) % 4 == 0
