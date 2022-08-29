#!/bin/bash

# Display the UID and Username of the user executing this script
# Display if the user is the root user or not

 
#Display UID

echo "Your UID is ${UID}"

#Display username
USER_NAME=$(id -un)
USER_NAME2=`id -un`

echo "Your username is $USER_NAME"
echo "Your username is $USER_NAME2"

# Display user root or not
if [[ "${UID}" -eq 0 ]]
then
    echo 'You are ROOT'
else
    echo 'You are NOT ROOT'
fi
