# Programer Name: Ani Ohanian
# Date:8/13/22
# Description: This program defines a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). 
# For example, is_palindrome("radar") should return True.


def is_palindrome(palindrome):
    result1 = ""
    result2 = ""
    for i in range(0, len(palindrome), 1):
        result1 += palindrome[i]
    for i in range(len(palindrome)-1,-1, -1):
        result2 += palindrome[i]
    if result1 == result2:
        return True
    else: 
        return False


userInput = input("Please enter your favorite word: ")
result = is_palindrome(userInput)
if result:
    print("The enterered word is palindrome.")
else:
    print("The entered word is Not palindrome.")