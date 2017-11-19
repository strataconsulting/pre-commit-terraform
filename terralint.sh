#!/usr/bin/env bash

set -x

LOGFILE=/tmp/terralint.log

# TerraLint doest work file by file. It analize the entire directory
# Therefore, take the base directory of the first file as argument
FILE1=$1
DIRECTORY=$(dirname "${FILE1}")

echo "FILE1=$FILE1" >> /tmp/terralint.log
echo "DIRECTORY=$DIRECTORY" >> /tmp/terralint.log

# Execute terralint.py providing the directory where the terraform file(s) are located
SCRIPTDIR=$(dirname "$0")
echo "SCRIPTDIR=$SCRIPTDIR" >> /tmp/terralint.log
python "${SCRIPTDIR}/terralint.py" "${DIRECTORY}" >> /tmp/terralint.log
