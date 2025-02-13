#include <Python.h>

static struct PyModuleDef calculator_module = {
    PyModuleDef_HEAD_INIT,
    "calculator",
    "A simple calculator module",
    -1,
    calculator_methods
};

static PyObject* calculator_add(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b))
        return NULL;
    return Py_BuildValue("d", a + b);
}
static PyObject* calculator_sub(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b))
        return NULL;
    return Py_BuildValue("d", a - b);
}
static PyObject* calculator_mul(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b))
        return NULL;
    return Py_BuildValue("d", a * b);
}

static PyObject* calculator_div(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b))
        return NULL;
    if (b == 0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "Cannot divide by zero");
        return NULL;
    }
    return Py_BuildValue("d", a / b);
}

static PyMethodDef calculator_methods[] = {
    {"add", calculator_add, METH_VARARGS, "Add two numbers"},
    {"sub", calculator_sub, METH_VARARGS, "Subtract two numbers"},
    {"mul", calculator_mul, METH_VARARGS, "Multiply two numbers"},
    {"div", calculator_div, METH_VARARGS, "Divide two numbers"},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC PyInit_calculator(void) {
    return PyModule_Create(&calculator_module);
}