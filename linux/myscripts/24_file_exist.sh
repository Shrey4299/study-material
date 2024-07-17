#!/bin/bash
FILEPATH="/home/adcuratio/Desktop/Study/linux/myscripts/prashant.test"
if [[ -f $FILEPATH ]]
then
echo "File exist"
else
echo "Creating_file now"
touch $FILEPATH
fi