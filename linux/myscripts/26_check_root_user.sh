#!/bin/bash

user=$UID

if [ $user -eq 0 ]; then
    echo "root user"
else
    echo "non-root user"
fi