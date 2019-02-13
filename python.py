#******** 16.CLASS ********
#		Class is a blueprint for how an object should look, it is not
#	an object itself, only describes how an object look and behave
#		Then we can create a new "Object" which is based on particular
#	class and that class is govern how the object behave, what methods
#	and what attributes it has.
# 	
#	To find type of the object
#	type(argument)
#	ex:	
#		type("string")
#		<class 'str'>
#******* creating class ********* 
#	
#	class Class_name:
#		def __init__(self):
#			self.attribute_name=attribute_value
#			self.attribute_name=attribute_value
#
#		def method_name(self):
#			//some code 			
#
#******** create object from the class ********
#	object_name=Class_name()
#

#creating class
class Person:
	def __init__(self):
		self.name="nanne"
		self.age=20
		self.study="b.tech"
	
	def printName(self):
		return f'Name is {self.name}'
	
	def printStudy(self):
		print(f"He is studing {self.study}")
		
#creating object	

Person1=Person()
print(Person1.name)
print(Person1.printName())
Person1.printStudy()

#creating another object

Person2=Person()
print("printing second object")
print("second object age ",Person2.age)