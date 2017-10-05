#Emerging Technologies
#Python Fundatmentals Problem Sheet
#Ríona Greally - G00325504

#5. Write a guessing game where the user must guess a secret number. After every guess the program tells the user whether their number was too large or too small. 
#At the end the number of tries needed should be printed. 
#It counts only as one try if they input the same number multiple times consecutively.


from random import randint

#using random module to generate random number and assigning it to x
x=(randint(0,10))

#assign num a number not between 0 & 10
num = -1

#creating list for users guesses
guesses =[]
count = 0

#loop until correct number is guessed
while(num != x):
	num=int(input("Enter number: "))
	print(x)
	if num > x:
		print("Too Large")
		if num not in guesses:
			count+=1
			#adding number to guess list
			guesses.append(num)
	elif num < x:
		print("Too Small")
		if num not in guesses:
			count+=1
			#adding number to guess list
			guesses.append(num)
		
print("Yaaay you got it " + str(count) + " guesses")
	
