""" Task definitions for invoke command line utility"""

import invoke
import pathlib
import sys
import os
import shutil
import re
import glob

on_win = sys.platform.startswith("win")


@invoke.task
def clean(c):
    """Remove any built objects"""
    for file_pattern in (
        "*.o",
        "*.so",
        "*.obj",
        "*.dll",
        "*.exp",
        "*.lib",
    ):
        for file in glob.glob(file_pattern):
            os.remove(file)
    for dir_pattern in "Release":
        for dir in glob.glob(dir_pattern):
            shutil.rmtree(dir)


def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))


@invoke.task()
def build_animal(c):
    """Build the shared library for the Animal C++ code"""
    print_banner("Building C++ Library Animal")
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++17 -fPIC Animal.cpp "
        "-o libAnimal.so "
    )
    print("* Complete")


#  uses -I . allows the #include "Animal.hpp" line in the wrapper code to be resolved.
def compile_python_module(cpp_name, extension_name):
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++17 -fPIC "
        "-undefined dynamic_lookup "
        "`python3-config --includes` "
        "-I . "
        "`python3 -m pybind11 --includes` "
        "{0} "
        "-o {1}`python3-config --extension-suffix` "
        "-L. -lanimal -Wl,-rpath,.".format(cpp_name, extension_name)
    )


@invoke.task(build_animal)
def build_pybind11(c):
    """Build the pybind11 wrapper library"""
    print_banner("Building PyBind11 Module")
    compile_python_module("pybind11_animal_wrapper.cpp", "animal")
    print("* Complete")


@invoke.task()
def test_pybind11(c):
    """Run the script to test PyBind11"""
    print_banner("Testing PyBind11 Module")
    invoke.run("python3 animal_test.py", pty=True)


@invoke.task(
    clean,
    build_animal,
    build_pybind11,
    test_pybind11,
)
def all(c):
    """Build and run all tests"""
    pass
