class HotBeverage():
	"""Just some hot water in a cup."""

	price = 0.30
	name = "hot beverage"

	def description(self):
		return "Just some hot water in a cup."
	
	def __str__(self):
		return(
		"""
name : %s
price : %s
description : %s
		""" % (self.name, self.price, self.description()))

class Coffee(HotBeverage):
	name = "coffe"
	price = 0.40
	def description(self):
	 return "A coffee, to stay awake."

class Tea(HotBeverage):
	name = "tea"
	price = 0.30
	def description(self):
	 return "Just some hot water in a cup."

class Chocolate(HotBeverage):
	name = "chocolate"
	price = 0.50
	def description(self):
	 return "Chocolate, sweet chocolate..."

if __name__ == '__main__':
	drink = HotBeverage()
	print(drink)
	c = Coffee()
	print(c)
	t = Tea()
	print(t)
	ch = Chocolate()
	print(ch)
