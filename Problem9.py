#Emerging Technologies
#Python Fundatmentals Problem Sheet
#Ríona Greally - G00325504

#9. Implement the square root function using Newton’s method. 
#In this case, Newton’s method is to approximate sqrt(x) by picking a starting point z and then repeating:
# z_next = z - ((z*z-x)/(2*z))
#To begin with, just repeat that calculation 10 times and see how close you get to the answer for various values (1, 2, 3, …). 
#Next, change the loop condition to stop once the value has stopped changing (or only changes by a very small delta). 
#How close are you to the math.sqrt value?

import math
from decimal import *

# Step 1: loop the newton eq. ten times

#def newton_sqroot(x,z):
#    count = 0
#    while count<10:
#        z_next = z - ((z*z-x)/(2*z))
#        count+=1
#        z = z_next
#    return z

# Step 2: loop the newton eq. until there is only a very small delta

def newton_sqroot(x,z):
    delta = 1
    #looping until delta changes by very small amount 
    while delta>0.0000000001:
        z_next = z - ((z*z-x)/(2*z))
        #getting the difference
        delta=abs(z-z_next)
        z = z_next
    return z

x = Decimal(input("Enter the number you wish to find the square root of: \n"))
z = Decimal(input("Enter your square root guess: \n"))

result = newton_sqroot(x,z)
sqroot = Decimal(math.sqrt(x))
difference = abs(result-sqroot) 
print(str(result) + " vs " + str(sqroot) + " = " + str(difference))
