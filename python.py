#******** 13. SCOPE ********
#	Scope define the area/zone of a variable can be accessed
#	The global variable can be accessed everywhere
#	The local variable can be accessed only with in the function
#	
var_global="global"

def print_var():
	var_global="local"
	# here the var_global is override with the local var_global
	# variable so it will print local
	print(var_global)
	
print_var()	

print(var_global)