#******** 17.The init Function ********
#		The init function is like a constructor, when we create the object
#	the init function(constructor) will be invoked.	
#		While creating a new object we didnt pass any argument but it takes
#	self as the defualt argument and we can also pass some other arguments
#	while creating the object
# 
#******* creating class ********* 
#	
#	class Class_name:
#		def __init__(self,arguments):
#			self.attribute_name=arguments
#
#		def method_name(self):
#			//some code 			
#
#******** create object from the class ********
#	object_name=Class_name(arguments)
#

#creating class
class Student:
	def __init__(self,name,age,study):
		self.name=name
		self.age=age
		self.study=study

	def getStudy(self):
		print("He is studying ",self.study)
		
#creating object	

student1=Student("nanne",20,"B.tech")
print("Name of the student",student1.name)
print("Age of the student",student1.age)
student1.getStudy()

#creating another object

student2=Student("john",22,"Degree")
print("Name of the student",student2.name)
print("Age of the student",student2.age)
student2.getStudy()