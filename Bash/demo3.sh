#!/bin/bash

# This script creates an account on the local system
# You will be prompted for the account name and password


# Ask for the user name 
read -p 'Enter the username to create: ' USER_NAME

# Ask for the real name
read -p 'Enter the real name to create: ' REAL_NAME


#Ask if the user wants the home directory 
#read -p Do you want the home directory created?Default is No(y/n):
# Set the user

useradd -c "${REAL_NAME}" -m "${USER_NAME}"

# Set the password for the user

passwd ${USER_NAME}

# for user del 

read -p 'Do you want to delete a user?(y/n) default is n: ' DEL

read -p "Enter the username you want to delete: " USER_DEL
if [[ ${DEL} == 'y']]
then
    echo "Deleting user..."
    userdel "${USER_DEL}"
fi
