#!/bin/bash 

# Display text hello

echo "hello"

# Assign a value to a variable

word='script'

# display the value of the variable

echo "$word"

# combine variable with hard-coded text

echo "This is a bash $word"

#Display the contents of the variable using an alternative method

echo "This is a shell ${word}"

#append text to the variable

echo "${word}ing is fun!"

# how NOT to append text to a variable
echo "$wording is fun"

#new variable
ENDING='ed'

echo "this is ${word}${ENDING}."

#Reassignment of a variable

ENDING='ing'

echo "${word}${ENDING} is fun!"

#Reassignment 
ENDING='s'

echo "You are going to write many ${word}${ENDING} in this class"
