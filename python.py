#******** 13. SCOPE ********
#	Scope define the area/zone of a variable can be accessed
#	The global variable can be accessed everywhere
#	The local variable can be accessed only with in the function
#	
var_global="global"

def print_var():
	global var_global
	var_global="local"
	
	# the global keyword is used to convert the local variable
	# into global variable
	
	print(var_global)
	
print_var()	

print(var_global)