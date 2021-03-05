#include <Python.h>

#include <shaderc/shaderc.h>

PyObject * meth_glsl(PyObject * self, PyObject * args, PyObject * kwargs) {
    static char * keywords[] = {"source", NULL};

    const char * code;
    Py_ssize_t size;

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "s#", keywords, &code, &size)) {
        return NULL;
    }

    shaderc_compile_options_t options = shaderc_compile_options_initialize();
    shaderc_compile_options_set_optimization_level(options, shaderc_optimization_level_performance);
    shaderc_compile_options_set_warnings_as_errors(options);

    shaderc_compiler_t compiler = shaderc_compiler_initialize();
    shaderc_compilation_result_t result = shaderc_compile_into_spv(
        compiler,
        code,
        size,
        shaderc_glsl_infer_from_source,
        "source",
        "main",
        options
    );

    if (shaderc_compilation_status status = shaderc_result_get_compilation_status(result)) {
        if (status == shaderc_compilation_status_invalid_stage) {
            PyErr_Format(PyExc_ValueError, "compile error\n\nmissing #pragma shader_stage(...)");
        } else {
            PyErr_Format(PyExc_ValueError, "compile error\n\n%s", shaderc_result_get_error_message(result));
        }
        return NULL;
    }

    PyObject * res = PyBytes_FromStringAndSize(
        shaderc_result_get_bytes(result),
        shaderc_result_get_length(result)
    );

    shaderc_result_release(result);
    shaderc_compiler_release(compiler);
    return res;
}

PyMethodDef module_methods[] = {
    {"glsl", (PyCFunction)meth_glsl, METH_VARARGS | METH_KEYWORDS, NULL},
    {},
};

PyModuleDef module_def = {PyModuleDef_HEAD_INIT, "glnext_compiler", NULL, -1, module_methods};

extern "C" PyObject * PyInit_glnext_compiler() {
    return PyModule_Create(&module_def);
}
