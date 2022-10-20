#!/bin/bash

# STEPS -->
# 1 ) Check for root account
# 2 ) Usage help
# 3 ) Disable by default 
#  4 ) options -d --> delete,  -r --> remove the home directory, -a archive the home directory in /archive folder if the folder does not exist then make the folder
# 5 ) accepts a list of usernames as arguments 
# 6 ) if uid is less than 1000 refuse to delete/disable
# 7 ) inform the user if the account was deleted/disabled
# 8 ) Display the username and any actions performed against the account 

remove_directory(){

}

if [[ "${UID}" -ne 0 ]]
then
    echo 'Please use SUDO or Root Priviledges'
    exit 1
fi

PARAMETERS="${#}"

if [[ "${PARAMETERS}" -lt 1 ]]
then
    echo "Usage: ${0} USERNAME 
    -a <archive home directory>
    -r <remove the home directory>
    -d <Delete/disable the account>"
    exit 1
fi

for USER_NAME in "${@}"
do
    