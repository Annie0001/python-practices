# Programer Name: Ani Ohanian
# Date:8/20/22
# Description: This program reads in 10 scores from a file, scores.txt
# 1. Write the 10 scores into another file.
# 2. Find the highest score and append it into the same file.
# 3. Find the lowest score and append it into the same file.
# 4. Find the average score and append it into the same file
# 5. Supporting Material-- scores.txt
 
# Jones Tom 94 99 96 74 56 33 65 89 87 85
# Thompson Frank 67 58 86 95 47 86 79 64 76 45
# Jackson Tom 95 97 94 87 67 84 99 45 99 87
# Jackson Michael 43 23 34 77 64 35 89 56 75 85
# Johnson Sara 84 93 64 57 89 99 74 64 75 91
# Colt Josh 84 93 64 57 70 99 74 63.5 75 91
# Freeman Michael 67 58 86 95 47 86 79 64 76 45
# Vick Schaub 43 23 34 77 64 35 89 56 75 85
# Philip Rivers 94 99 96 74 56 33 65 89 87 85
# Matt Hassel 87 78 86 95 47 86 79 64.75 76 45
# beck Jimmy 43 86 34 77 64 35 89 56 75 85
# Clausen Joe 74 93 64 57 70 99 74 67 75 91
# Flacco Kyle 94 99 96 74 56 78 65 89 87 85
# Orton Jason 80 75 96 74 56 33.5 65 89 87 85

fileRead = open("scores.txt",'r')
fileWrite = open("scoresResults.txt",'w')
fileWrite.write("\t\t\t\t\t\t\t\tMax\t\tMin\t\tAverage\n")
for i in fileRead:
    lineItem = i.split()
    print(lineItem)
    floatList=[]
    sum = 0 
    for j in range(2,len(lineItem)):
        fileWrite.write(lineItem[j])
        fileWrite.write(" ")
        itemFloat = float(lineItem[j])
        floatList.append(itemFloat)
        sum += itemFloat
    fileWrite.write(" ")
    # finds and writes the max into the scoreResults.txt
    fileWrite.write(str(max(floatList)))
    fileWrite.write("\t\t")
    # finds and writes the min into the scoreResults.txt
    fileWrite.write(str(min(floatList)))
    fileWrite.write("\t\t")

    fileWrite.write(str(sum/len(floatList)))

    fileWrite.write("\n")
fileRead.close()
fileWrite.close()
    

