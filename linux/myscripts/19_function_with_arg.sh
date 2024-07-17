#!/bin/bash

num1=12
num2=13

sum=$((num1+num2))
echo "the sum of $num1 and $num2: $sum"

addition() {
    sum=$(( $1 + $2 ))
    echo "Addition: $1 + $2 = $sum"
}

subtraction() {
    diff=$(( $1 - $2 ))
    echo "Subtraction: $1 - $2 = $diff"
}

multiplication() {
    prod=$(( $1 * $2 ))
    echo "Multiplication: $1 * $2 = $prod"
}

division() {
    if [ $2 -ne 0 ]; then
        quot=$(( $1 / $2 ))
        echo "Division: $1 / $2 = $quot"
    else
        echo "Error: Division by zero is not allowed."
    fi
}

# Example usage
addition 20 30
subtraction 50 20
multiplication 5 6
division 40 8
division 10 0
