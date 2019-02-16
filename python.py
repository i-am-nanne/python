#********** 22. MAPS ********
#		Maps are way to take a list apply some kind of function
#	to each item in the list to change the items and splitout
#	new list from these updated items within it
#
#	map(function,data)
#

#comprehension way to square the items in a list
def square(num):
	return num*num

nums=[1,2,3,4,5]
square_nums=[square(num) for num in nums]
print(square_nums)


#Normal way to square the items in a list

#def square(num):
#	return num*num

#nums=[1,2,3,4,5,6,7,8,9]
#square_nums=[]
#for num in nums:
#	square_nums.append(square(num))

#print(square_nums)