#******** 13. SCOPE ********
#	Scope define the area/zone of a variable can be accessed
#	The global variable can be accessed everywhere
#	The local variable can be accessed only with in the function
#	

var_global="Printing the global variable"

def print_var():
	print(var_global)
	
print_var()	
print(var_global)