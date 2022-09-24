# Week 01: Q5.py, Programming Exercise
# This program asks the user for a number 'n' and gives the user the choice to compute the sum or factorial
# Author: Ross Downey

# Function for Total
def total(n):
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    print(sum)

# Function for Product
def factorial(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    print(product)

# Request input from user
n = 0
num = int(input("Please enter a number: "))
choice = int(input("If you would like the sum of the range 1 to n enter '1' if you would like the product of the same range enter '2'"))

# Calling previous functions depending on user's input
if choice == 1:
     total(num)
elif choice == 2:
    factorial(num)
else:
    print("Please enter a valid choice")