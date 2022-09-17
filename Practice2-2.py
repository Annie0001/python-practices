# Programer Name: Ani Ohanian
# Date:7/23/22
# Description: This program asks for the names of three runners and the time it took each of them to ﬁnish a race.
# The program should display who came in ﬁrst, second, and third place. Think about how many test cases are needed to verify 
# that your problem works correctly.

firstRunner = input("Please enter the 1st runner name: ")
secondRunner = input("Please enter the 2nd runner name: ")
thirdRunner = input("Please enter 3rd runner name: ")

firstRunnerTime = float(input("How long did it take for the first runner to finish the race? "))
secondRunnerTime = float(input("How long did it take for tthe second runner to finish the race? "))
thirdRunnerTime = float(input("How long did it take for the third runner to finish the race? "))

if firstRunnerTime < secondRunnerTime:
    if firstRunnerTime < thirdRunnerTime:
        print(firstRunner, "came in first. ")
        if secondRunnerTime < thirdRunnerTime:
            print(secondRunner, "came in second. ")
            print(thirdRunner, "came in third. ")
        else:
            print(thirdRunner, "came in second. ")
            print(secondRunner, "came in third. ")
    else:
        print(thirdRunner, "came in first. ")
        print(firstRunner,  "came in second. ")  
        print(secondRunner, "came in third. ") 
else:
    if secondRunnerTime < thirdRunnerTime:
        print(secondRunner, "came in first. ")
        if firstRunnerTime < thirdRunnerTime:
            print(firstRunner, "came in second. ")
            print(thirdRunner, "came in third. ")
        else:
            print(thirdRunner, "came in second.")
            print(firstRunner, "came in third. ")
    else:
        print(thirdRunner, "came in first. ")
        print(secondRunner,"came in second. ")
        print(firstRunner, "came in third. ")

        
