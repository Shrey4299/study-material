#!/bin/bash

# Example of a for loop to iterate through an array of fruits
fruits=("Apple" "Banana" "Orange" "Grapes")

echo "Printing fruits using for loop:"
for fruit in "${fruits[@]}"
do
    echo "Fruit: $fruit"
done
