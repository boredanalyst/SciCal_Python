##SCIENTIFIC CALCULATORS

# Importing modules and libraries

import math


# Declaring the main menu:

main_menu = {1:"Basic Operations",2:"Advanced Arithmetic",3:"Trigonometric Functions"}

# Declaring the sub-menus
basic_menu = {1:"Add",2:"Subtract",3:"Multiply",4:"Divide",5:"Modulus"};
advanced_menu = {1:"Square root",2:"Natural Logarithm",3:"Logarithm Base 10", 4:"Exponent"};
trig_menu = {1:"Sine",2:"Cosine",3:"Tangent"}

# Setting up the menus

def showMainMenu():
  try:
    print("--------------------------------------")
    print("MAIN MENU")
    print("Please provide the number assigned to the menu you want to open.")
    for x in main_menu:
      print(str(x) + ": " + main_menu[x])
    user_input = int(input("Input your choice here: "))
    if user_input == 1:
      showBasicMenu();
    elif user_input == 2:
      showAdvMenu();
    elif user_input == 3:
      showTrigMenu();
    else: 
      print("Please provide a valid number.")
      showMainMenu()
  except ValueError:
    print("Please provide a valid number.")
    showMainMenu()

def showBasicMenu():
  try:
    print("--------------------------------------")
    print("BASIC OPERATIONS")
    print("Please provide the number assigned to the option you want to use:")
    for x in basic_menu:
      print(str(x) +": " + basic_menu[x])
    user_input = int(input("Input your choice here: "))
    if user_input == 1:
      add()
    elif user_input == 2:
      subtract()
    elif user_input == 3:
      multiply()
    elif user_input == 4:
      divide()
    elif user_input == 5:
      modulus()
    else: 
      print("Please provide a valid number.")
      showMainMenu()
  except ValueError:
    print("Please provide a valid number.")
    showBasicMenu()

def showAdvMenu():
  try:
    print("--------------------------------------")
    print("ADVANCED ARITHMETIC")
    print("Please provide the number assigned to the option you want to use:")
    for x in advanced_menu:
      print(str(x) +": " + advanced_menu[x])
    user_input = int(input("Input your choice here: "))
    if user_input == 1:
      sqRoot()
    elif user_input == 2:
      logZero()
    elif user_input == 3:
      logTen()
    elif user_input == 4:
      exponent()
    else: 
      print("Please provide a valid number.")
      showMainMenu()
  except ValueError:
    print("Please provide a valid number.")
    showAdvMenu()

def showTrigMenu():
  try:
    print("--------------------------------------")
    print("TRIGONOMETRIC FUNCTIONS")
    print("Please provide the number assigned to the option you want to use:")
    for x in trig_menu:
      print(str(x) +": " + trig_menu[x]) 
  except ValueError:
    print("Please provide a valid number.")
    showTrigMenu()

## Setting up the operations.

def add():
  print("--------------------------------------")
  print("ADDITION");
  try:
    num1 = float(input("Please provide your first number: "))
    print(num1);
    num2 = float(input("Please provide your second number: "))
    print(str(num1) + " + " + str(num2))
    print(f'Answer: {num1 + num2}')
  except ValueError:
    print("Error: Your input should be a valid number.")
    add()

def subtract():
  print("--------------------------------------")
  print("SUBTRACTION");
  try:
    num1 = float(input("Please provide your first number: "))
    print(num1);
    num2 = float(input("Please provide your second number: "))
    print(str(num1) + " - " + str(num2))
    print(f'Answer: {num1 - num2}')
  except ValueError:
    print("Error: Your input should be a valid number.")
    subtract()

def multiply():
  print("--------------------------------------")
  print("MULTIPLICATION");
  try:
    num1 = float(input("Please provide your first number: "))
    print(num1);
    num2 = float(input("Please provide your second number: "))
    print(str(num1) + " * " + str(num2))
    print(f'Answer: {num1 * num2}')
  except ValueError:
    print("Error: Your input should be a valid number.")
    multiply()

def divide():
  print("--------------------------------------")
  print("DIVISION");
  try:
    num1 = float(input("Please provide your first number: "))
    print(num1);
    num2 = float(input("Please provide your second number: "))
    print(str(num1) + " / " + str(num2))
    print(f'Answer: {num1 / num2}')
  except ValueError:
    print("Error: Your input should be a valid number.")
    divide()
  except ZeroDivisionError:
    print("Error: You cannot divide a number by zero.")

def modulus():
  print("--------------------------------------")
  print("MODULUS");
  try:
    num1 = float(input("Please provide your first number: "))
    print(num1);
    num2 = float(input("Please provide your second number: "))
    print(str(num1) + " % " + str(num2))
    print(f'Answer: {num1 % num2}')
  except ValueError:
    print("Error: Your input should be a valid number.")
    modulus()

## Setting up advanced operations

## Square Root function


def sqRoot():
  print("--------------------------------------")
  print("SQUARE ROOT");
  try:
    user_input = float(input("Input a number: "))
    print(user_input);
    print(f'Square root: {math.sqrt(user_input)}')
  except ValueError:
    print("One of the values you provided is not a valid number.")
    sqRoot()

## Natural Logarithm function

def logZero():
  print("--------------------------------------")
  print("NATURAL LOGARITHM");
  try:
    user_input = float(input("Input a number: "))
    print("-->" + str(user_input));
    print(f'Natural Logarithm: {math.log(user_input)}')
  except ValueError:
    print("One of the values you provided is not a valid number.")
    logZero()

## Logarithm base 10 function

def logTen():
  print("--------------------------------------")
  print("LOGARITHM BASE 10");
  try:
    user_input = float(input("Input a number: "))
    print("-->" + str(user_input));
    print(f'Natural Logarithm: {math.log10(user_input)}')
  except ValueError:
    print("One of the values you provided is not a valid number.")
    logTen()

## Exponentiation function

def exponent():
  print("--------------------------------------")
  print("EXPONENTIATION");
  try:
    num1 = float(input("Input the base number: "))
    print("-->" + str(num1));
    exp = float(input("Input the exponent: "))
    print("-->" + str(num1) + " raised to " + str(exp))
    print(f'Answer: {num1 ** exp}')
  except ValueError:
    print("One of the values you provided is not a valid number.")
    exponent()

## Setting up trigonometric functions.

## Sine function (must use degrees.)

def sine():
  print("--------------------------------------")
  print("SINE");
  try:
    user_input = float(input("Input a number with degree units: "))
    print(f'Degrees: {str(user_input)} --> Radians: {math.radians(user_input)}');
    print(f'Sine: {math.sin(math.radians(user_input))}')
  except ValueError:
    print("One of the values you provided is not a valid number.")
    sine()

## Cosine function (must use degrees.)

def cosine():
  print("--------------------------------------")
  print("COSINE");
  try:
    user_input = float(input("Input a number with degree units: "))
    print(f'Degrees: {str(user_input)} --> Radians: {math.radians(user_input)}');
    print(f'Cosine: {math.cos(math.radians(user_input))}')
  except ValueError:
    print("One of the values you provided is not a valid number.")
    cosine()

## Tangent function (must use degrees.)

def tangent():
  print("--------------------------------------")
  print("COSINE");
  try:
    user_input = float(input("Input a number with degree units: "))
    print(f'Degrees: {str(user_input)} --> Radians: {math.radians(user_input)}');
    print(f'Tangent: {math.tan(math.radians(user_input))}')
  except ValueError:
    print("One of the values you provided is not a valid number.")
    tangent()

###---------------------------------------------------------------------------------------###

showMainMenu()