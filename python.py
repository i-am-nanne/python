#******** 13. SCOPE ********
#	Scope define the area/zone of a variable can be accessed
#	The global variable can be accessed everywhere
#	The local variable can be accessed only with in the function
#	

def print_var():
	var_local="Printing the local variable"
	print(var_local)
	
print_var()	

#	here we get error because var_local variable is a local 
#	variable and it is available only with in the function
#	so we can not access out side of the function

print(var_local)