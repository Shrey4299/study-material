#!/bin/bash
#example of using continue in loop
# Suppose we only need to print odd no.
for i in 1 2 3 4 5 6 7 8 9 10
do
let r=$i%2
if [[ $r -eq 0 ]]
then
continue
fi
echo "odd no. is $i"
done

for i in 1 2 3 4 5 6 7
do
if [[ $i -eq 6 ]]
then
echo "6 is present"
break
fi

done