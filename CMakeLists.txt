cmake_minimum_required(VERSION 3.14)
cmake_policy(SET CMP0148 NEW)  # Suppress FindPythonInterp warning

project(backend_module)

# Use C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Fetch pybind11 from GitHub
include(FetchContent)
FetchContent_Declare(
  pybind11
  GIT_REPOSITORY https://github.com/pybind/pybind11.git
  GIT_TAG        v2.11.1
)
FetchContent_MakeAvailable(pybind11)

# Build Python module
pybind11_add_module(backend_module
    bindings/pybackend.cpp
)

# Include backend headers
target_include_directories(backend_module PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/base
    ${CMAKE_CURRENT_SOURCE_DIR}/metrics
)

# Link required libraries
target_link_libraries(backend_module PRIVATE
    pthread
)
