# Week 01: Q3.py, Programming Exercise
# This program asks the user for a number 'n' and prints the sum of the numbers 1 to n,
# Author: Ross Downey

n = int(input ("Please enter a number:"))
# New variable to add the sum of numbers to, starting at 0
total = 0
# While loop, iterated down to zero by adding the previous integer to the total variable
while n > 0:
    total += n
    n -= 1
print ("The sum of the numbers 1 to n is:", total)

