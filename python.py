#************** 20. Bar Tab Calculator *********
#
#

class Tab:
	menu={
		"wine":5,
		"beer":3,
		"soft_drink":2,
		"chicken":10,
		"beef":15,
		"veggie":12,
		"desert":6
	}

	def __init__(self):
		self.total=0
		self.items=[]

	def add(self,item):
		self.items.append(item)
		self.total=self.total+self.menu[item]

	def printBill(self,tax,service):
		tax=(tax/100)*self.total
		service=(service/100)*self.total
		total=self.total+tax+service

		for item in self.items:
			print(f"{item:10} ${self.menu[item]}")
		print(f"{'service':10} ${service}")
		print(f"{'tax':10} ${tax}")
		print(f"{'Total':10} ${total}")

table1=Tab()
table1.add("wine")
table1.add("beef")
table1.printBill(10,10)