# Programer Name: Ani Ohanian
# Date:8/13/22
# Description: This program declares two empty lists one is for name and one for salaries. 
# Within the for loop ask for employees name and their salaries and append them into the list accordingly. 
# Find out the total salary using accumulation concept but you need to call a function called EvaluateSalary()
# within the for loop passing the argument salary for each iteration.
# Output : Both of the lists with their items and the total salary.

employeeName = []
employeeSalaries = []
totalSalary = 0

numberOfEmployee = int(input("Please enter for how many employees are you asking: "))

def EvaluateSalary(salary):
    global totalSalary
    totalSalary += salary
    return totalSalary

for employee in range(numberOfEmployee):

    name = input("Please enter your name: ")
    salary = float(input("Please enter your salary: "))
    employeeName.append(name)
    employeeSalaries.append(salary)
    result = EvaluateSalary(salary)

print(employeeName)
print(employeeSalaries)
print(round(result,2))
