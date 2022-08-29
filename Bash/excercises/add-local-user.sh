#!/bin/bash

# Check if the user is sudo or not
if [[ "${UID}" -eq 0 ]]
then
    echo 'ROOT PRIV'

else
    echo 'You are NOT ROOT. Please use SUDO'
    exit
fi

read -p 'Enter New USERNAME: ' USER_NAME
read -p 'Enter REAL NAME: ' REAL_NAME

useradd -c "${REAL_NAME}" -m "${USER_NAME}"
read -p 'Enter the Password: ' PASS
passwd ${USER_NAME}

echo "Your USERNAME is: ${USER_NAME}"
echo "Your PASSWORD is: ${PASS}"

