#!/bin/bash

# This script demonstrates I/O redirection

#Redirect STDOUT to a file 

FILE="/tmp/data"
head -n1 /etc/passwd > ${FILE}

#Redirect STDIN to a file 

read LINE < ${FILE} 
echo "${LINE}"

#Redirect STDOUT to a file, overwriting the file.
echoecho "Contents of ${FILE}:"
cat ${FILE}

#Redirect STDOUT to a file , appending to the file.

echo "${RANDOM} ${RANDOM}" >> ${FILE}
echo "${RANDOM} ${RANDOM}" >> ${FILE}
echo
echo "Contents :"
cat ${FILE}
