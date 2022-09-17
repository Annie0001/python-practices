# Programer Name: Ani Ohanian
# Date:7/28/22
# Description: This program asks the user to enter the amount spent on electricity and Gas bill for 3 consecutive months. 
# Count and display the number of  months where the user went over budget if the electricity bill is over $45 dollars 
# and Gas bill is over $30 dollars. 

monthCount = 0

electricityBill1 = float (input("Please enter your first month electricity bill amount here: $"))
if(electricityBill1 < 0):
    print("Please eneter a non-negative number.")
    exit()
gasBill1 = float (input("Please enter your first month gas bill amount here: $"))
if(gasBill1 < 0):
    print("Please eneter a non-negative number.")
    exit()
electricityBill2 = float (input("Please enter your second month electricity bill amount here: $"))
if(electricityBill2 < 0):
    print("Please eneter a non-negative number.")
    exit()
gasBill2 = float (input("Please enter your second month gas bill amount here: $"))
if(gasBill2 < 0):
    print("Please eneter a non-negative number.")
    exit()
electricityBill3 = float (input("Please enter your third month electricity bill amount here: $"))
if(electricityBill3 < 0):
    print("Please eneter a non-negative number.")
    exit()
gasBill3 = float (input("Please enter your third month gas bill amount here: $"))
if(gasBill3 < 0):
    print("Please eneter a non-negative number.")
    exit()
    
if (electricityBill1 > 45 and gasBill1 > 30):
    monthCount += 1
if (electricityBill2 > 45 and gasBill2 > 30):
    monthCount += 1
if (electricityBill3 > 45 and gasBill3 > 30):
    monthCount += 1

if (monthCount == 0): 
    print ("Your monthly bills are within the budget.")
else:
    print("You went over budget for", monthCount, "month(s).")