#********** 26. Reading files ********

file=open("text.txt")
file.seek(0)
#read takes numbers of chareters to read
print(file.read(10))
file.close()