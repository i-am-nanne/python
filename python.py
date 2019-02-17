#********** 26. Reading files ********

text_file=open("text.txt")
#store the each line as item in the list
lines=text_file.readlines()
print(lines)
text_file.close()