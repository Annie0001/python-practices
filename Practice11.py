# Programer Name: Ani Ohanian
# Date:8/20/22
# Description: This program reads in from a ﬁle a starting month name, an ending month name,
# and then the monthly rainfall for each month during that period. As it does this, it should
# sum the rainfall amounts and then report the total rainfall and average rainfall for the
# period. For example, the output might look like this:  
# During the months of March–June the total rainfall was 7.32 inches and the average
# monthly rainfall was 1.83 inches.
# Data for the program can be found in the Rainfall.txt ﬁle.
# Hint: After reading in the month names, you will need to read in rain amounts until
# the EOF is reached, and count how many pieces of rain data you read in.

# Using notepad you can create a data file called Rainfall.txt with the following data.

# June
# September
# 2.35     1.15     2.03     1.41

fileRead = open("Rainfall.txt")
line = 1
sum = 0
for i in fileRead:
    if line == 3:
        lineItem = i.split()
        print(lineItem)
        for j in lineItem:
            sum += float(j)
    line +=1
fileRead.close()
print("Sum is: "+format(sum,'.2f')+"\nMonthly rainfall average is: "+ format((sum/len(lineItem)),'.2f'))