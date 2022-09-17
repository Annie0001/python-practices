# Programer Name: Ani Ohanian
# Date:8/06/22
# Description: This program declares two empty lists one is for name and one for salaries.
# Within the for loop ask for employees name and their salaries and append them into the list accordingly.
# Find out the total salary using accumulation concept.
# Output : Both of the lists with their items and the total salary.

nameList = []
salaryList = []
totalSalary = 0

numberOfEmployees = int(input("Please enter number of employees: "))

for employeeInfo in range(numberOfEmployees):
    employeeName = input("Please enter your name: ")
    employeeSalary = float(input("Please enter your salary: "))
    nameList.append(employeeName)
    salaryList.append(employeeSalary)
    totalSalary += employeeSalary
print("Name of the employees: ",nameList ,"Salary of the employees: ",salaryList ,"The total salary for all the employees:", totalSalary)
