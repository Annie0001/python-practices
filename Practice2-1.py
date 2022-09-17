# Programer Name: Ani Ohanian
# Date:7/23/22
# Description: This program will have a user to enter a number. 
# Write some conditional statement to check whether the number entered by the user is even or odd.

try:
    number = int(input("Please enter a number: "))
    if number % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")
except:
    print("You entered an invalid value.")
