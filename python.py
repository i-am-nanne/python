#************** 21. List Comprehensions *********
#	

#Normal way to double the list values
nums=[12,11,43,15,30]
double_nums=[]
for num in nums:
	double_nums.append(num*2)
print(nums)
print(double_nums)

#comprehension way to double the list values

nums_comp=[20,2,3,8,19]
double_nums_comp=[ num*2 for num in nums_comp ]
print(nums_comp)
print(double_nums_comp)