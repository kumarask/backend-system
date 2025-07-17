cmake_minimum_required(VERSION 3.15)
project(backend_system)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Enable pybind11
find_package(pybind11 REQUIRED)

# Include headers
include_directories(${CMAKE_SOURCE_DIR}/include)

# Source files
file(GLOB_RECURSE SOURCES
    ${CMAKE_SOURCE_DIR}/src/*.cpp
)

# Build the Python module
pybind11_add_module(backend_module ${SOURCES})

# Optional: Link with other libraries if needed
# target_link_libraries(backend_module PRIVATE some_lib)
