"""********** 25. DECORATORS ********
	Decorators basically extends the behaviour of functions,that
ussued on without modifying the function itself
	
	def decorator_name(function):
		def wrapper_function():
			//code to execute before the function
			function()
			//code to execute after the function
		return wrapper_function
	
	@decorator_name
	def function():
		//code

	@decorator_name
"""

def wish(s):
	def wrapper():
		print("welcome to the city")
		s()
		print("Thank you for visiting ! visit again")

	return wrapper()

@wish
def jmd_city():
	print("This is jmd city")

@wish
def pdtr_city():
	print("This is pdtr city")