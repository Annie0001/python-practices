# Programer Name: Ani Ohanian
# Date:7/21/22
# Description: This program will be used to design a mobile phone app which allows a user to press a button that starts a 
# timer that counts seconds.When the user presses the button again, the timer stops. After drawing the flowchart and 
# write pseudocode,code the program that accepts the elapsed time in seconds and displays the value in minutes and 
# remaining seconds.For example, if the elapsed time was 130 seconds, the output would be 2 minutes and 10 seconds.


elapseTimeInSeconds = int(input("Please enter the number of seconds: "))


elapseTimeMinutes = int(elapseTimeInSeconds // 60)
elapseTimeSeconds = int(elapseTimeInSeconds % 60)

print("elapsed time is: ",elapseTimeMinutes , "minutes","and",elapseTimeSeconds,"seconds")