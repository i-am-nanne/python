#	if(condition):
#		code to execute
#	elif(condition):
#		code to execute
#	.	
#	.
#	etc
#	else(condition):
#		code to execute

#	Python follows indent format so we need to statement should be
#		indented

num=int(input("Enter the number "))
if(num<=100):
	print("The inputed number is less than or equal to 100")
elif(num<=200):
	print("The inputed number is less than or equal to 200")
else:
	print("The number is greater than 100 and 200")