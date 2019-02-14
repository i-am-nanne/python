#******** 18.Methods and Attributes ********
#	Attributes:
#		1.instance attributes
#		2.class attributes
#
#	Methods:
#		1.instance methods
#		2.class Methods ( @classmethod )
#		3.static methods ( @staticmethod )
#
#
#	class Class_name:
#		class_variable_name=class_variable_value
#		def __init__(self,arg):
#			self.variable_name=arg
#		
#		def instance_Method(self):
#			//some code to execute
#
#		@classmethod
#		def class_method_name(cls):
#			//some code to execute
#
#		@staticmethod
#
#		def static_method_name(arg):
#			//some code to execute
#
#
#	NOTE:
#	->	The instance methods and instance attributes can be accesed only by using
#	the object name
#	->	The class methods and class attributes can be accesed by both object name
#	and class name
#	-> The static methods can be accesed by both object name and class name

class Student:
	#class attribute
	college="IIIT RK valley"

	def __init__(self,name,age,study):
		#instance attributes
		self.name=name
		self.age=age
		self.study=study

	#instance methods
	def getStudy(self):
		print("He is studying",self.study)

	#class method
	@classmethod
	def getCollege(cls):
		print(f"He is studying in {cls.college}")

	#static method
	@staticmethod
	def aboutStudies(performance="good"):
		print("He is studying ",performance)


#creating object

student1=Student("nanne",20,"B.tech")
#printing instance attributes
print(student1.name)
print(student1.age)

#printing class attributes using object name
print(student1.college)

#printing class attributes using class name
print(Student.college)

#printing the instance method
student1.getStudy()

#printing class methods using object name
student1.getCollege()

#printing class methods using class name
Student.getCollege()

#printing static methods using the object name
student1.aboutStudies()

#printing static methods using the class name
Student.aboutStudies()



















