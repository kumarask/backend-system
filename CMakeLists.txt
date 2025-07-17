cmake_minimum_required(VERSION 3.14)
cmake_policy(SET CMP0148 NEW)  # Avoid deprecated FindPython warning

project(backend_module)

# Enable C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Download and configure pybind11 using FetchContent
include(FetchContent)
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG        v2.11.1
)
FetchContent_MakeAvailable(pybind11)

# Define the Python module using pybind11
pybind11_add_module(backend_module
    bindings/bindings.cpp
)

# Include directories for your backend source
target_include_directories(backend_module PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/base
    ${CMAKE_CURRENT_SOURCE_DIR}/metrics
)

# Link pthread for multithreaded support
target_link_libraries(backend_module PRIVATE pthread)
