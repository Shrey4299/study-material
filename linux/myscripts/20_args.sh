#!/bin/bash

# to access the arguments

echo "First argument is $1"
echo "Second argument is $2"
echo "Number of arguments is $#"
echo "All arguments are is $@"

for filename in $@
do
    echo "coping file $filename"
done