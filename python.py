"""********** 24. LAMBDAs ********
	Lamdas are bit like anonymous function which means they
don't have a name or any kind of identifier
syn:
	lambda argument,argument:
		/code
ex:
	lambda x,y:
		x*y

	it is same as

	def mul(x,y):
		return x*y

"""
# normal way to square the list items

def square(num):
	return num*num

nums=[1,2,3,4,5]
print(list(map(square,nums)))