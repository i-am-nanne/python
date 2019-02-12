#******** 14. DICTIONARIES ********
#		Dictionary is a mapping type , basically it is a set
#	of key value pair

#	{key:value,key:value ...... key:value}
#					or
#	dict(key=value,key=value ...... key=value)

#printing the dictionary
def print_dict(dictionary):
	for key,value in dictionary.items():
		print(f'name : {key} and age : {value}')

person={}
while(True):
	name=input("Enter the name ")
	age=int(input("Enter the age "))
	person[name]=age
	
	one_more=input("Do you want to add another ? (y/n) ")
	if(one_more=='n'):
		break

print_dict(person)