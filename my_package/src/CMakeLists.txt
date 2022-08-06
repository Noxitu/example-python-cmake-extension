cmake_minimum_required(VERSION 3.10)

project(my_package)

find_package(pybind11 REQUIRED)

pybind11_add_module(
    ${PROJECT_NAME} MODULE
    "src/lib.cpp"
)

add_subdirectory(noxitu)
