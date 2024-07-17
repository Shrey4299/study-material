#!/bin/bash

read -p "Enter a number: " num

# Check if the number is greater than 10 and even
if [[ $num -gt 10 ]] && [[ $((num % 2)) -eq 0 ]]
then
  echo "$num is greater than 10 and even."
fi

# Check if the number is less than 5 or odd
if [[ $num -lt 5 || $((num % 2)) -ne 0 ]]
then
  echo "$num is either less than 5 or odd."
fi
