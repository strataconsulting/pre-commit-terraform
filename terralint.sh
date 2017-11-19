#!/usr/bin/env bash

set -x

# TerraLint doest work file by file. It analize the entire directory
# Therefore, take the base directory of the first file as argument
FILE1=$1
DIRECTORY=$(dirname "${FILE1}")

# Execute terralint.py providing the directory where the terraform file(s) are located
SCRIPTDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
python "${SCRIPTDIR}/terralint.py" "${DIRECTORY}"
