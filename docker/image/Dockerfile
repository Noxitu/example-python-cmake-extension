FROM python:3.10

RUN apt-get update && \
    apt-get install -y \
        cmake

RUN python -m venv /virtualenv && \
    /virtualenv/bin/pip install \
        conan \
        numpy

RUN /virtualenv/bin/conan install -r conancenter pybind11/2.10.0@_/_
