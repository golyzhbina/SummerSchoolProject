#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#define PY_SSIZE_T_CLEAN

#include <Python.h>
#include <ndarraytypes.h>
#include <ndarrayobject.h>
#include <numpyconfig.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>


static double* calc_cube(size_t* dimsTFAS, PyArrayObject* timesForAllSourceArr, size_t* dimsTraces, PyArrayObject* tracesArr, int time_start, int time_finish){

    size_t len_of_interval = (size_t)(time_finish - time_start);
    double* cube = (double*)malloc(len_of_interval * dimsTFAS[0] * sizeof(double));
    memset(cube, 0, sizeof(double) * dimsTFAS[0] * len_of_interval);

    for (size_t i = 0; i < dimsTFAS[0]; ++i){
        for (size_t j = 0; j < dimsTFAS[1]; ++j){
            int indexInTrace = *((int*)PyArray_GETPTR2(timesForAllSourceArr, i, j));
            for (size_t k = 0; k < len_of_interval; ++k){
                cube[len_of_interval * i + k] += *((double*)PyArray_GETPTR2(tracesArr, j, indexInTrace));
                ++indexInTrace;
            }
        }
    }
    return cube;
}


static PyObject* geo_create_cube(PyObject *self, PyObject *args){

    PyArrayObject* timesForAllSource;
    PyArrayObject* traces;
    int time_start, time_finish;

    if (!PyArg_ParseTuple(args, "OOii", &timesForAllSource, &traces, &time_start, &time_finish))
        return NULL;
    

    size_t* dimsTFAS = (size_t*)PyArray_DIMS(timesForAllSource);
    size_t* dimsTraces = (size_t*)PyArray_DIMS(traces);

    double* cube = calc_cube(dimsTFAS, timesForAllSource, dimsTraces, traces, time_start, time_finish);

    npy_intp const dims[2] = {(npy_intp)dimsTFAS[0], (npy_intp)(time_finish - time_start)}; 

    return PyArray_SimpleNewFromData(2, dims, NPY_DOUBLE, cube);
}

static PyMethodDef GeoMethods[] = {
    {"create_cube",  geo_create_cube, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cubemodule = {
    PyModuleDef_HEAD_INIT,
    "geo",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    GeoMethods
};

PyMODINIT_FUNC PyInit_geo(void) {
    import_array();
    return PyModule_Create(&cubemodule);
}

int main(int argc, char const *argv[])
{
	if (PyImport_AppendInittab("geo", PyInit_geo) == -1) {
        //std::cerr << "Error: could not extend in-built modules table" << std::endl;
        exit(1);
    }

    PyStatus status;
    PyConfig config;
    PyConfig_InitPythonConfig(&config);

    status = PyConfig_SetString(&config, &config.program_name, (const wchar_t*)argv[0]);
    if (PyStatus_Exception(status)) {
        PyConfig_Clear(&config);
        Py_ExitStatusException(status);
    }

    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {
        PyConfig_Clear(&config);
        Py_ExitStatusException(status);
    }


    Py_Initialize();
    PyObject *pmodule = PyImport_ImportModule("geo");
    if (!pmodule) {
        PyErr_Print();
        //std::cerr << "Error: could not import module 'main'" << std::endl;
    }

	return 0;
}