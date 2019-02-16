#********** 23. FILTERS ********
#		Filters gives us an easy way to take a collection
#	and filter out some other values based on function result
#	this gives us filter colletion

# Normal way to find the even numbers in a list

nums=[1,2,3,4,5,6,7,8,9,10]
evenNums=[]
for num in nums:
	if(num%2==0):
		evenNums.append(num)
print(evenNums)