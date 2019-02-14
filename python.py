#************* 19. Modules and Packages **********
#	Module:	Just a python file
#	Package : Collection of modules
#
#	To import the module there are two ways:
#	1.
#		import module_name(nothing but filename)
#		#to use the functions or values in the moudle
#		module_name.function_name() (or) module_name.variable_name
#		
#	2.
#		from module_name import * (# to import all)
#		from module_name import specific_function_name
#		specific_function_name()
#
#

import module_example

print(module_example.add(10,20))
print(module_example.sub(20,10))
print(module_example.mult(10,20))