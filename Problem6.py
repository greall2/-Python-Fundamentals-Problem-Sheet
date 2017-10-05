#Emerging Technologies
#Python Fundatmentals Problem Sheet
#Ríona Greally - G00325504

#6. Write a function that returns the largest and smallest elements in a list.

#creating a list
list =[]

#assigning the userinput to length
length = int(input("How long do you want the list?"))

count = 0

while count < length:
	userInput = int(input("Enter nummber :" ))

	#adding user input to the list
	list.append(userInput)
	count +=1


smallest = min(list)
largest = max(list)

#printing smallest and largest numbers in list
print("Smallest: " +str(smallest) + " Largest: " + str(largest))
