# Programer Name: Ani Ohanian
# Date:8/13/22
# Description: This program will create a calculator.
# create a function menu with different options as following: (Output sample is below)
# main menu, and prompts for a choice
# Welcome to calculator.py
# your options are:
# 1) Addition
# 2) Subtraction
# 3) Multiplication
# 4) Division
# 5) Quit calculator.py
# Choose your option: 
# When user choose the options 1-4, the appropriate functions will be called to do addition, 
# subtraction, Multiplication, and Division or quit the program.


total = 0
menuOptions = 1
def additionFunc(numberAddition):
    global total
    total += numberAddition
def subtractionFunc(numberSubtract):
    global total
    total -= numberSubtract
def multiplicationFunc(numberMultiplication):
    global total
    total *= numberMultiplication
def divisionFunc(numberDivision):
    global total
    total /= numberDivision
    
print("Welcome to calculator.py")

while ( menuOptions != 5):
    print("total= " , total)
    userInput = int(input("Please enter a number: "))
    menuOptions = int(input("1) Addition " + "2)Subtraction " + "3)Multiplication " + "4)Division " + "5)Quit calculator.py:  "))

    if menuOptions == 1:
        additionFunc(userInput)
    elif menuOptions == 2:
        subtractionFunc(userInput)
    elif menuOptions == 3:
        multiplicationFunc(userInput)
    elif menuOptions == 4:
        divisionFunc(userInput)


