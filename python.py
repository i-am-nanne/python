#************** 21. List Comprehensions *********
#	

#Normal way to square the even nums only
nums=[1,2,3,4,5,6,7,8,9]
square_nums=[]
for num in nums:
	if(num**2%2==0):
		square_nums.append(num**2)
print(nums)
print(square_nums)

#comprehension way to square the even nums only

nums_comp=[1,2,3,4,5,6,7,8,9]
square_nums_comp=[ num**2 for num in nums_comp if num**2%2==0 ]
print(nums_comp)
print(square_nums_comp)