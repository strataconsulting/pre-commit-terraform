#!/usr/bin/env bash

# TerraLint doest work file by file. It analize the entire directory
# Therefore, take the base directory of the first file as argument
DIRECTORY=$(dirname $1)

# Execute terralint.py providing the directory where the terraform file(s) are located
python ./terralint.py $DIRECTORY
