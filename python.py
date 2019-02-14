#************* 19. Modules and Packages **********
#	Module:	Just a python file
#	Package : Collection of modules
#	
#	Module:
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
#	Package:
#		For creating a package we need to choose a folder then we add a file named
#	__init__.py file and then we add the python files that are going to be used
#	as modules
#	
#	To import the package
#	from package_name.module_name import *
#
#

from test.module_example import *
from test.print_some_stuff import *
print(add(20,50))
print(sub(50,20))
print(mult(20,50))
print("invoking the the fun function")
fun()
print("invoking the getAuthorName function")
getAuthorName()