#Emerging Technologies
#Python Fundatmentals Problem Sheet
#Ríona Greally - G00325504

#10. Write a function to reverse a string.

#using extended slice with a negative value as the step parameter and return reversed string
def reversed_string(a_string):
    return a_string[::-1]

userInput = input("Enter string to test: ")

#printing out result
print(reversed_string(userInput))