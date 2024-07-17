#!/bin/bash

#monitoring the free fs space disk
FU=$(df -H | grep "dev/nvme0n1p1" | awk '{print $5}' | tr -d %)
if [[ $FU -ge 10 ]]
then
echo "Warning, disk space is low"
else
echo "All good"
fi
