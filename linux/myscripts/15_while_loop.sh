#!/bin/bash

# Example of a while loop to count from 1 to 5
count=1

echo "Counting from 1 to 5 using while loop:"
while [ $count -le 5 ]
do
    echo "Count: $count"
    ((count++))
done
