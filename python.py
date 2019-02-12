#******** 15.SET ********
#	A set is a collection of data(A bit like list) , they dont
#	allow duplicates
#	>>> nums=[1,2,3,4,1,2,3]
# 	>>> set(nums)
#		[1,2,3,4]

def belt_count(dictionary):
	belts=list(dictionary.values())
	for belt in set(belts):
		num=belts.count(belt)
		print(f"There are {num} {belt} belts")
		
ninja_belts={}

while(True):
	ninja_name=input("Enter a ninja name  ")
	ninja_belt=input("Enter a belt color ")
	ninja_belts[ninja_name]=ninja_belt
	
	another=input("Add another ? (y/n) ")
	if(another=='n'):
		break
	
belt_count(ninja_belts)