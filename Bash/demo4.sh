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
echo -e 'Hash SHA256 passthrou: echo "$PASSWORD" | sha256sum'


