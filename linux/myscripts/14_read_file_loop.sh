#!/bin/bash

# Define the file path
File="/home/adcuratio/Desktop/Study/linux/myscripts/names.txt"

# Check if the file exists
if [[ ! -f $File ]]; then
    echo "File not found!"
    exit 1
fi

# Read each name from the file and print it
for name in $(cat $File)
do
    echo "Names: $name"
done

