Simple package, using `cmake` to build a `cpython` extension. Uses `conan` to download `pybind11` as C++ dependency.

`my_package` contains all the required setup that should allow for use as normal package.
 - `pip install ./my_package` to install.
 - `python -m build ./my_package` to build both source distribution with C++ source code (will still invoke conan) and a binary wheel.

 Additionally, a root `CMakeLists.txt` with `.vscode/settings.json` is provided to set up a CMake build directory that outputs libraries into `editable` directory - to be used with `pip install -e ./editable`.
 