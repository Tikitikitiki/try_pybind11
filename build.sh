#!/bin/zsh
mkdir -p build
cd build
echo "Generate Makefiles for the project"
cmake .././CMakeLists.txt
echo "Build project"
cmake --build .
echo "Build project success"
libAnimal=animal$(python3-config --extension-suffix)
cp ${libAnimal} ../src