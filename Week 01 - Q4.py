# Week 01: Q4.py, Programming Exercise
# This program asks the user for a number 'n' and prints the sum of the numbers 1 to n,
# with only multiples of 3 and 5 being considered in the sum
# Author: Ross Downey

n = int(input ("Please enter a number:"))
# New variable to add the sum of numbers to, starting at 0
total = 0

# Setting range 1 to n
for i in range(1,n):
    # Only incuding multiples of 3 and 5 using modulo (remainder = 0) function
    if (i % 3 == 0 or i % 5 == 0):
        total = total + i
print ("The sum of the numbers, that are multiples of 3 or 5, in the range 1 to n is:",total)

