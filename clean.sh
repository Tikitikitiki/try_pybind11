#!/bin/zsh
# if build directory exists, then remove it
[ -d "./build" ] && rm -r build
cd src
invoke clean