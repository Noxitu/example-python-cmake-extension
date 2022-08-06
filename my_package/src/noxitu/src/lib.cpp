#include <pybind11/pybind11.h>

template<typename T>
auto mul(T i, T j) {
    return i * j;
}

PYBIND11_MODULE(my_package, m) {
    m.doc() = "pybind11 example plugin";

    m.def("mul", &mul<int>, "A function that multiplies two numbers");
    m.def("mul", &mul<float>, "A function that multiplies two numbers");
}
