#include <pybind11/pybind11.h>

template<typename T>
auto add(T i, T j) {
    return i + j;
}

PYBIND11_MODULE(my_package, m) {
    m.doc() = "pybind11 example plugin";

    m.def("add", &add<int>, "A function that adds two numbers");
    m.def("add", &add<float>, "A function that adds two numbers");
}
