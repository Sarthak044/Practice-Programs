#!/bin/bash

# Make sure the script is being executed with superuser privileges.
if [[ "${UID}" -eq 0 ]]
then
    echo 'ROOT PRIV'

else
    echo 'You are NOT ROOT. Please use SUDO'
    exit
fi


# If the user doesn't supply at least one argument, then give them help.

# The first parameter is the user name.
# Generate a password.
# Create the user with the password.
# Check to see if the useradd command succeeded.
# Set the password.
# Check to see if the passwd command succeeded.
# Force password change on first login.
# Display the username, password, and the host where the user was created.

#same code as add-local-user.sh