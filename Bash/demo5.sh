# to reset the hash table for PATH we use hash -r

echo "${0}"

# Display the path and filename of the script.

echo "You used $(dirname ${0}) as the path to the $(basename ${0}) script."


# How many arguments they passed in.
# (inside the script they are parameters, outside they are arguments.)

NUMBER_OF_PARAMETERS="${#}"
echo "You supplied ${NUMBER_OF_PARAMETERS} argument(s) on the command line."

# Make sure they atleast supply one argument

if [[ "${NUMBER_OF_PARAMETERS}" -lt 1 ]]
then
    echo "Usage: ${0} USERNAME [USERNAME] .. "
    exit 1
fi
