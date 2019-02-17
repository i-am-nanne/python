#********** 27. Write files ********
l=[
	"hello this is example\n",
	"hello this is another example\n",
	"hello this is third example\n"
]
with open("write.txt","w") as write_file:
	write_file.writelines(l)