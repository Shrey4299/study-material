#!/bin/bash

# Define the file path
File="/home/adcuratio/Desktop/Study/linux/myscripts/test.csv"

# Check if the file exists
if [[ ! -f $File ]]; then
    echo "File not found!"
    exit 1
fi

# Read the CSV file line by line
while IFS=, read -r id name age
do
    # Skip the header line
    if [[ $id == "id" ]]; then
        continue
    fi
    
    echo "ID: $id, Name: $name, Age: $age"
done < "$File"
