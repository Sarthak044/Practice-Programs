#!/bin/bash

# This script generates a list of random passwords.


# Random number as a password

PASSWORD=${RANDOM}

echo "$PASSWORD"

# Three random numbers together 

PASSWORD="${RANDOM}${RANDOM}${RANDOM}"
echo "$PASSWORD"

# use the current date/time as the basis for the password 

PASSWORD=$(date +%s%N)         # %s --> seconds %N --> nanoseconds
echo "$PASSWORD"  # we can also pipe this to hash function like sha256sum
#Hash SHA256 passthrou: head 
echo "$PASSWORD" | sha256sum

# A better Password 

PASSWORD=$(date +%s%N | sha256sum | head -c12)
echo "$PASSWORD"

# An even better password
PASSWORD=$(date +%s%N${RANDOM}${RANDOM} | sha256sum | head -c12)
echo "${PASSWORD}"

# speacial char

special_char=$(echo '!@#$%^&*()-+=' | fold -w1 | shuf | head -c1)
special_char2=$(echo '!@#$%^&*()-+=' | fold -w1 | shuf | head -c1)


#shuf command "man shuf"

# shuf /etc/passwd

# fold command "man fold"

# append a special char

echo "${special_char2}${PASSWORD}${special_char}"