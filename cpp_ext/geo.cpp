#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#define PY_SSIZE_T_CLEAN

#include <Python.h>
#include <ndarraytypes.h>
#include <ndarrayobject.h>
#include <numpyconfig.h>
#include <cstring>
#include <stdlib.h>


static double* calc_cube(size_t* dimsTFAS, long long* time, size_t* dimsTraces, double* traces, int time_start, int time_finish){

    size_t len_of_interval = (size_t)(time_finish - time_start);
    double* cube = new double[dimsTFAS[0] * len_of_interval];
    memset(cube, 0, sizeof(double) * dimsTFAS[0] * len_of_interval);

    for (size_t i = 0; i < dimsTFAS[0]; ++i){
        for (size_t j = 0; j < dimsTFAS[1]; ++j){
            int indexInTrace = time[i * dimsTFAS[1] + j];
            for (size_t k = 0; k < len_of_interval; ++k){
                cube[len_of_interval * i + k] += traces[j * dimsTraces[1] + indexInTrace];
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
    
    size_t* dimsTraces = (size_t*)PyArray_DIMS(traces);
    PyArrayObject* tracesCContArr = (PyArrayObject*)PyArray_FROM_OTF((PyObject*)traces, NPY_DOUBLE, NPY_ARRAY_C_CONTIGUOUS);
    if (tracesCContArr == NULL){
        PyErr_SetString(PyExc_RuntimeError, "could not get C_CONTIGUOUS array from traces");
        return NULL;
    }
    double* tracesArr = (double*)PyArray_DATA(tracesCContArr);

    size_t* dimsTFAS = (size_t*)PyArray_DIMS(timesForAllSource);
    PyArrayObject* timesForAllSourceCContArr = (PyArrayObject*)PyArray_FROM_OTF((PyObject*)timesForAllSource, NPY_INT64, NPY_ARRAY_C_CONTIGUOUS);
    if (timesForAllSourceCContArr == NULL){
        PyErr_SetString(PyExc_RuntimeError, "could not get C_CONTIGUOUS array from time_for_all_source");
        Py_DECREF(tracesCContArr);
        return NULL;
    }
    long long* timeArr = (long long*)PyArray_DATA(timesForAllSourceCContArr);

    double* cube = calc_cube(dimsTFAS, timeArr, dimsTraces, tracesArr, time_start, time_finish);

    npy_intp const dims[2] = {(npy_intp)dimsTFAS[0], (npy_intp)(time_finish - time_start)}; 
    PyArrayObject* cubeArr = (PyArrayObject*)PyArray_SimpleNewFromData(2, dims, NPY_DOUBLE, cube);
    PyArray_ENABLEFLAGS(cubeArr, NPY_ARRAY_OWNDATA);

    Py_DECREF(tracesCContArr);
    Py_DECREF(timesForAllSourceCContArr);

    return (PyObject*)cubeArr;
}

static PyMethodDef GeoMethods[] = {
    {"create_cube",  geo_create_cube, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef geomodule = {
    PyModuleDef_HEAD_INIT,
    "geo",
    NULL, 
    -1,       
    GeoMethods
};

PyMODINIT_FUNC PyInit_geo(void) {
    import_array();
    return PyModule_Create(&geomodule);
}

int main(int argc, char const *argv[])
{
	if (PyImport_AppendInittab("geo", PyInit_geo) == -1) {
        std::cerr << "Error: could not extend in-built modules table" << std::endl;
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
        std::cerr << "Error: could not import module 'geo'" << std::endl;
    }

	return 0;
}