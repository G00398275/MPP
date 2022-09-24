# Week 01: Q7.py, Programming Exercise
# This program prints all prime numbers smaller than 100
# Author: Ross Downey


# For loop in required range
for x in range(1,101):
    prime = True
    for i in range(2,x):
        if (x % i== 0): # Using modulo function to determine if number is a prime or not
            prime = False
    if prime == True: # If it is a prime number then print it
       print (x)

