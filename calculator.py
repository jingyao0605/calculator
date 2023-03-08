#!/usr/bin/env python
# coding: utf-8

# # Team7
# 
# ### Members:
#  - Jingyao Wang
#  - Vu Quang Dan
#  - Truong Hoang Thong
#  - Rinkal Kalubhai Dhameliya
#  - Thennakoon Mudiyanselage Shamila Harshani Theennakoon
#  
#  

# ### Topic: Tic-Tac-Toe
# #### Task
# - To build a basic calculator program in Python that allows the user to perform various mathematical operations.
# 
# ### Goal
# - The goal of this project is to provide a user-friendly interface that allows users to perform basic mathematical operations, including addition, subtraction, multiplication, division, second power, and square root. The program should provide a menu for the user to select the desired operation and allow them to perform the operation as many times as they want until they choose to exit the program
# 
# 

# In[ ]:


import math

def add(x, y):
    """Adds two numbers"""
    return x + y

def subtract(x, y):
    """Subtracts two numbers"""
    return x - y

def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def divide(x, y):
    """Divides two numbers"""
    return x / y

def square(x):
    """Returns the square of a number"""
    return x ** 2

def square_root(x):
    """Returns the square root of a number"""
    return math.sqrt(x)

# Display the menu to the user
while True:
    print("                          ")
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Second power")
    print("6. Square root")
    print("7. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1-7): ")

    # Perform the selected operation
    if choice == '7':
        print("Exiting the program...")
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "to the power of 2 =", square(num1))
            print(num2, "to the power of 2 =", square(num2))

        elif choice == '6':
            if num1 < 0 or num2 < 0:
                print("Error: Cannot calculate square root of negative number")
            else:
                print("Square root of", num1, "=", square_root(num1))
                print("Square root of", num2, "=", square_root(num2))

    else:
        print("Invalid input, please try again.")




# 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




