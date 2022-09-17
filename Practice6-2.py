# Programer Name: Ani Ohanian
# Date:7/29/22
# Description: This program is designed for  West LA College. 
# 1 - Assume the current tuition is $15,000 per year, and tuition is expected to increase by 4 percent each year.
#     Display the tuition each year for the next 10 years.
# 2 - Modify the West LA College program so that the user enters the rate of tuition increase instead of having it fixed at 4 percent.
# 3 - Modify the West LA College program so that the user enters the rate of tuition increase for the first year. 
#     The rate then increases by 0.5 percent each subsequent year.

currentTuition = 15000
rateOfTuitionIncrease= float(input("Please enter the rate of tuition increase: "))

for numberOFYear in range(10):
    currentTuition += (currentTuition * (rateOfTuitionIncrease/100))
    print("Your tuition for end of year", (numberOFYear+1) ,"is: $" , round(currentTuition,2))