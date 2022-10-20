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

# Redirect STDINto a program, using File descriptor 0

read LINE 0< ${FILE}
echo
echo "LINE CONTAINS: ${LINE}"

#Redirect STDOUT to a file using FIle Descriptor 1, overwriting the file 
head -n3  /etc/passwd   1> ${FILE}
echo
echo "Contents of the ${FILE}: "
cat ${FILE}

#Redirect  STDERR to a file using File DEscriptor 2

ERR_FILE="/tmp/data.err"
head -n3 /etc/passwd /fakefile 2> ${ERR_FILE}
cat ${ERR_FILE}

# Redirect STDOUT and STDERR to a file 
head -n3 /etc/passwd /fakefile &> ${FILE}
echo
echo "COntents of ${FILE}:"
cat ${FILE}

#Redirect STDOUT and STDERR through a pipe.
echo
head -n3 /etc/passwd /fakefile |& cat -n

# Discard STDOUT via /dev/null
echo
echo "Discarding STOUT:"
head -n3 /etc/passwd /fakefile > /dev/null

#Discard STDERR 
echo
echo "Discarding STDERR:"
head -n3 /etc/passwd /fakefile 2> /dev/null

#Discard both STDOUT & STDERR
echo
echo "Discarding both STDOUT & STDERR:"
head -n3 /etc/passwd /fakefile &> /dev/null

# Clean Up
rm ${FILE} ${ERR_FILE} &>/dev/null