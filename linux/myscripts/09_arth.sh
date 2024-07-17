#!/bin/bash

# Variables
num1=10
num2=5

# Addition
sum=$((num1 + num2))
echo "Addition: $num1 + $num2 = $sum"

# Subtraction
difference=$((num1 - num2))
echo "Subtraction: $num1 - $num2 = $difference"

# Multiplication
product=$((num1 * num2))
echo "Multiplication: $num1 * $num2 = $product"

# Division
quotient=$((num1 / num2))
echo "Division: $num1 / $num2 = $quotient"

# Modulus (remainder of division)
remainder=$((num1 % num2))
echo "Modulus: $num1 % $num2 = $remainder"

# Increment
((num1++))
echo "Increment: num1++ = $num1"

# Decrement
((num2--))
echo "Decrement: num2-- = $num2"

# Complex expression
complex_expression=$(( (num1 + num2) * (num1 - num2) ))
echo "Complex expression: (num1 + num2) * (num1 - num2) = $complex_expression"
