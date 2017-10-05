
#Emerging Technologies
#Python Fundatmentals Problem Sheet
#Ríona Greally - G00325504

#4. Factorial digit sum
#Write a function that calculates the sum of the digits of the factorial of a number. 
#n! means n x (n − 1) … x 3 x 2 x 1. For example, 10! = 10 x 9 x … x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. 
#Find the sum of the digits in the number 100!

# function to calculate the factorial
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
        
#retrieving number from user
num=int(input("Enter number: "))

#printing factorial of number inputted by user
print(factorial(num))