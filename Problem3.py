#Emerging Technologies
#Python Fundatmentals Problem Sheet
#Ríona Greally - G00325504

# 3 FizzBuzz
#Write a program that prints the numbers from 1 to 100, except for the following conditions. 
#For multiples of three print “Fizz” instead of the number, and for the multiples of five print “Buzz”. 
#For numbers which are multiples of both three and five print “FizzBuzz”.

#looping through numbers from 1 to 100
for i in range (100):
	# Numbers that are multiples of 3 then print "Fizz"
	if i % 3 == 0:
		print("Fizz")
	# Numbers that are multiples of 5 print out "Buzzz"
	elif i % 5 == 0:
		print("Buzz")
	# Numbers that are multiple of both 3 & 5
	elif (i % 3) & (i % 5):
		print("FizzBuzz")
	else:
		print(i)

