#******** 12. FUNCTIONS ********
#	They are basically used for creating a block of code which
#	can be used and called upon when we needed
#	
#	def function_name():
#		code to execute	
#	 
#	def function_name(arguments):
#		code to execute
#
#	def function_name(arguments=default_value):
#		code to execute
#	
#	def function_name():
#		code to execute
#		return some_value
#

def square(num):
	return num*num
	
temp=square(10)
print(temp)