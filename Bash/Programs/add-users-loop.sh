#!/bin/bash

# Goal:
# The goal of this exercise is to create a shell script that adds users to the same Linux system as the script is executed on.

# Make sure the script is being executed with superuser privleges.

if [[ "${UID}" -eq 0 ]]
then
    echo '<<ROOT>>'

else
    echo 'You are NOT ROOT. Please use SUDO'
    exit
fi


# If the user doesn't supply at least one argument, then give them help.

NUMBER_OF_PARAMETERS="${#}"
if [[ "${NUMBER_OF_PARAMETERS}" -lt 1 ]]
then
    echo "Usage: ${0} USERNAME .. "
    exit 1
fi

for USER_NAME in "${@}"
do
    PASSWORD=$(date +%s%N | sha256sum | head -c20)
    echo "Your USERNAME AND PASSWORD ARE AS FOLLOWS KINLDY NOTE DOWN >>"
    echo "USERNAME: ${USER_NAME}"
    echo "PASWORD: ${PASSWORD}"
done

useradd -m -U "${USER_NAME}"
echo "$USER_NAME:$PASSWORD" | chpasswd

if [[ ${?} -eq 0 ]]
then
    echo "Success"
    exit
else
    echo "Not Successfull. TRY AGAIN"
    exit
fi
