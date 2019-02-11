#	while(condition):
#		code to execute
#	
#	white(condition):
#		if(condition):
#			break
#	
#	while(condition):
#		if(condition):
#			continue
#	
#********INFINITE LOOP **********
#	while(True):
#	  code to execute


#printing even numbers below 10

s=0
e=20
while(s<=e):
	if(s==0):
		s=s+1
		continue
	if(s%2==0):
		print(s)
	if(s==10):
		break
	s=s+1