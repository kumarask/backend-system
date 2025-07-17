cmake_minimum_required(VERSION 3.14)
project(backend_module)

set(CMAKE_CXX_STANDARD 17)

# Fetch pybind11 directly from GitHub
include(FetchContent)
FetchContent_Declare(
  pybind11
  GIT_REPOSITORY https://github.com/pybind/pybind11.git
  GIT_TAG        v2.11.1  # Or latest stable
)
FetchContent_MakeAvailable(pybind11)

add_subdirectory(${pybind11_SOURCE_DIR} ${pybind11_BINARY_DIR})

pybind11_add_module(backend_module bindings/pybackend.cpp)
target_include_directories(backend_module PRIVATE ../base ../metrics)
target_link_libraries(backend_module PRIVATE pthread)
