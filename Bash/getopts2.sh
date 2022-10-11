#!/bin/bash

echo "Number of args: ${#}"
echo "All args: ${@}"
echo "First arg: ${1}"
echo "Second arg: ${2}"
echo "Third arg: ${3}"

# Inspect OPTIND
echo "OPTIND: ${OPTIND}"