#!/bin/bash
# How to store the key values pairs.
declare -A myArray
myArray=( [name]="Prashant" [age]=28 [city]="Paris" )
echo "Name is ${myArray[name]}"
echo "Age is ${myArray[age]}"

