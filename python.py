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

age=int(input("Enter the age "))
if(age>=18):
	print("You can apply for voter id")
else:
	print("Sorry!, you can not apply for voter id")