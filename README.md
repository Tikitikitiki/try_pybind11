# How to test pybind11, packaging a cpp class into a python library called animal

## Use python virtual environment

### Create python virtual environment
Stand at try_pybind11 root level, run:

    python3 -m venv .

### Activate python virtual environment
Macos / Linux:

    source ./bin/activate

Windows:

    source Scripts/activate

### Install packages in the requirement list

    pip install -r requirements.txt

### Verify the installed packages

    pip list

## Build python library
There are two ways to build python library, building it using cmake, or building it manually
with the help of invoke tool, prefarably using cmake.

### Build python library using cmake
Build the libary using cmake, then test using the new python library animal.

    ./build.sh
    cd src
    python3 animal_test.py

Clean out the build folder and the library, stand at try_pybind11 root level, run:

    ./clean.sh

### Build python library manually (not recommended)
Standing on try_bind11/src level, run `invoke --list` to see all the possible tasks,
run each tasks individually `invoke <task_name>`, or run all the tasks at once, including testing the new
python library animal.

    invoke all

Clean out the build folder and the library, stand at try_pybind11 root level, run:

    ./clean.sh