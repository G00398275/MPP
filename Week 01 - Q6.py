# Week 01: Q6.py, Programming Exercise
# This program prints a multiplication table for numbers up to 12
# Author: Ross Downey

# Request input from user
num = int(input(" Please enter the number: "))

print("The multiplication table of:", num)
# Range from 1 to 12 using for loop and print in correct output
for i in range(1, 13):
   print(i,"X",num,"=",num * i)