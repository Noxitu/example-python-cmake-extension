cmake_minimum_required(VERSION 3.10)

project(noxitu__my_package)

find_package(pybind11 REQUIRED)

pybind11_add_module(
    ${PROJECT_NAME} MODULE
    "src/lib.cpp"
)

if (DEFINED CMAKE_LIBRARY_OUTPUT_DIRECTORY)
    set(PYTHON_PACKAGE_NAME "my_package")
    set(PYTHON_PACKAGE_PATH "noxitu")

    set_target_properties(
        ${PROJECT_NAME}
        PROPERTIES
            OUTPUT_NAME "${PYTHON_PACKAGE_NAME}"
            LIBRARY_OUTPUT_DIRECTORY "${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/${PYTHON_PACKAGE_PATH}"
    )
endif()