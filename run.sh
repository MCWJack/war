#! /bin/bash
readarray -t RESULT < <(./war.py -d)
a="${RESULT[0]}"
b="${RESULT[1]}"
c="${RESULT[2]}"
d="./war.py -1 \"$a\" -2 \"$b\""

echo $a
echo $b
echo $c

END=100
for ((i=1;i<=END;i++)); do
    eval $d
done

