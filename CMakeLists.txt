cmake_minimum_required(VERSION 3.15.1)
project(Animal)
set(CMAKE_CXX_STANDARD 17)

execute_process(
    COMMAND bash -c "python3 -m pybind11 --cmakedir"
    OUTPUT_VARIABLE pybind11_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
set(pybind11_DIR ${pybind11_DIR})

#add_subdirectory(${pybind11_DIR})
find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(animal src/pybind11_animal_wrapper.cpp src/Animal.hpp src/Animal.cpp)

