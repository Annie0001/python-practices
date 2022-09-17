# Programer Name: Ani Ohanian
# Date:7/29/22
# Description: This program finds the square of numbers from 1-10 using for loop.
# Hint: The operator for square is **
# Sample Output:

# number          square
#========================
#   1             1
#   2             4
#   3             9
#   4             16
#   5             25
#   6             36
#   7             49
#   8             64
#   9             81
#   10           100

print("#"+" "+ "number"+"\t"+"square")
print("#=======================")
for i in range (1 ,11 , 1):
    numberSquare = i**2
    print("#",i," \t \t ",numberSquare)
