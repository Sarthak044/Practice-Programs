#!/bin/bash

# This script generates a random password
# User can set the password lenth with -l
# User can set special character with -s
# User can set verbose mode with -v

usage(){
    echo "Usage: ${0} [-vs] [-l LENGTH]" >&2
    echo 'Generate a random password.'
    echo ' -l Specify the password length.'
    echo ' -s Append a special character to the password.'
    echo ' -v Verbose Mode.'
    exit 1
}

info(){
    local MESSAGE="${@}"
    if [[ "${VERBOSE}" = 'true' ]]
    then
        echo "${MESSAGE}"
    fi
}

# Defualt length
LENGTH=48

while getopts vl:s OPTION
do
    case ${OPTION} in 
        v)
            VERBOSE='true'
            info 'Verbose mode on'
            ;;
        l)
            LENGTH="${OPTARG}"
            ;;
        s)
            USE_SPECIAL_CHAR='true'
            ;;
        ?)
            usage
            ;;
    esac
done

info 'Generating password'

PASSWORD=$(date +%s%N${RANDOM}${RANDOM} | sha256sum | head -c${LENGTH})

# Append a special Char
if [[ "${USE_SPECIAL_CHAR}" = 'true' ]]
then
    info 'Selecting a random special character.'
    SPECIAL_CHAR=$(echo '!@#$%^&*()-+=' | fold -w1 | shuf | head -c1)
    PASSWORD=${PASSWORD}${SPECIAL_CHAR}
fi

info 'Done.'
info 'Here is the Password.'

# Display the password 
echo "${PASSWORD}"
