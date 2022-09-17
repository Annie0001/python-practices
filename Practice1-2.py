# Programer Name: Ani Ohanian
# Date:7/21/22
# Description: This program allows the user to enter values for a salesperson’s base salary, 
# total sales, and commission rate. The program computes and outputs the salesperson’s pay by adding the base salary to 
# the product of the total sales and commission rate. 

baseSalary = float(input("Please enter your base salary: "))
totalSale = float(input("Please enter your total sale: "))
commissionPercentage = float(input("Please enter your commision rate in percentage: "))
commissionRate = float(commissionPercentage / 100)

salesPersonPay = (baseSalary + (totalSale * commissionRate))

print("Your pay is:" , float(salesPersonPay))