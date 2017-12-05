#!/usr/bin/env bash

# Although pre-commit-terraform works file by file, TFRules validates an entire directory
# Therefore, here we get the base directory of the first file provided as argument
FILE1=$1
DIRECTORY=$(dirname "${FILE1}")

# Execute tfrules.py providing the directory where the terraform file(s) are located
SCRIPTDIR=$(dirname "$0")
python "${SCRIPTDIR}/tfrules.py" "${DIRECTORY}"
