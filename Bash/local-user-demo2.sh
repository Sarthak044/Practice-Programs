#!/bin/bash

# Display the UID and username of the user executing this script
# DIsplay if the user is sk user or not

# Display the UID

echo "Your UID is ${UID}"

# Only display id the UID does NOT match 1000

UID_TO_TEST_FOR='1000'
if [[ "${UID}" -ne "${UID_TO_TEST_FOR}" ]]
then 
    echo "Your UID does not match ${UID_TO_TEST_FOR}"
    exit 
else
    echo "Your UID matches which is ${UID_TO_TEST_FOR}"
fi

#Display username

USER_NAME=$(id -un)

# Test if the command succeeded

if [[ "${?}" -ne 0 ]] #${?} --> stores the latest exit status
then 
    echo 'The id command did not execute successfully'
    exit 1
fi

echo "Your username is ${USER_NAME}"

# You can use a string test conditional 

USER_NAME3='sk'

if [[ "${USER_NAME}" = "${USER_NAME3}" ]]
then
    echo "Your username matches ${USER_NAME3}"
fi

# Test for != (not equal) for string

