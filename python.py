#******** 11. RANGES ********
#	
#	range(start,stop,step)
#
# 	when you pass three values to range it consider first value
# 	as start point and second value as end point(which is not 
# 	inclued) and third value as step(increament) 

burgers=["beef","chicken","veg","supreme","double"]
for r in range(len(burgers)):
	print(r,burgers[r])
