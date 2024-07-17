#!/bin/bash

read -p "Enter your choice (a, b, c): " choice

case $choice in
  a)
    echo "You chose 'a'."
    echo "Executing 'date' command:"
    date
    ;;
  b)
    echo "You chose 'b'."
    echo "Executing 'ls' command:"
    ls
    ;;
  c)
    echo "You chose 'c'."
    echo "Executing 'pwd' command:"
    pwd
    ;;
  *)
    echo "Invalid choice: Please enter a, b, or c."
    ;;
esac

