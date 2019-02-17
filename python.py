#********** 26. Reading files ********

text_file=open("text.txt")
for line in text_file:
	print(line.rstrip())

text_file.close()