#Emerging Technologies
#Python Fundatmentals Problem Sheet
#Ríona Greally - G00325504

#7. Write a function that tests whether a string is a palindrome.

# adapted from https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python

#reversing string, compare with original string and return result
def ispalindrome(userInput):
	return userInput == userInput[::-1]

userInput = input("Enter string to test: ")

#printing True/False 
print(ispalindrome(userInput))