#Emerging Technologies
#Python Fundatmentals Problem Sheet
#Ríona Greally - G00325504


# Write a program that prints the current time and date to the console.



import datetime

#retriveing the current date and tine
current = datetime.datetime.now()

## outputting the date and time in dd/mm/yyyy format
print ("Current Time and Date : " + current.strftime("%H:%M:%S %d/%m/%Y"))


