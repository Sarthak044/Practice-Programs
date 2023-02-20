NUMBER_OF_PARAMETERS="${#}"

if [[ "${NUMBER_OF_PARAMETERS}" -lt 1 ]]
then
    echo "Usage: ${0} NAME-OF-FILE.asm .. "
    exit 1
fi

for FILE in "${@}"
do
    echo "Assembly Compiling Via NASM"
    nasm -felf64 ${FILE} -o ${FILE}'.o'
done