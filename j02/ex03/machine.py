from beverages import HotBeverage, Tea
import random

class CoffeeMachine():

	def __init__(self):
		super().__init__()
		self.broke = 0

	class EmptyCup(HotBeverage):
		name = "empty cup"
		price = 0.90

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")
			raise Exception("This coffee machine has to be repaired.")

	def repair(self):
		self.broke = 0
	
	def serve(self, obj):
		try:
			if self.broke == 10:
				self.BrokenMachineException()
			else:
				b = random.getrandbits(1)
				self.broke += 1
				if b:
					return obj
				else:
					return self.EmptyCup()
		except Exception:
			print("This coffee machine has to be repaired.")


if __name__ == '__main__':
	machine = CoffeeMachine()
	t = Tea()
	print(machine.serve(t))
	print(machine.serve(t))
	print(machine.serve(t))

	print(machine.serve(t))
	print(machine.serve(t))
	print(machine.serve(t))

	print(machine.serve(t))
	print(machine.serve(t))
	print(machine.serve(t))

	print(machine.serve(t))
	print(machine.serve(t))
	print(machine.serve(t))
	machine.repair()
	print(machine.serve(t))
	print(machine.serve(t))
	print(machine.serve(t))
	print(machine.serve(t))

	print(machine.serve(t))
	print(machine.serve(t))
	print(machine.serve(t))

	print(machine.serve(t))
	print(machine.serve(t))
	print(machine.serve(t))

	print(machine.serve(t))
	print(machine.serve(t))
	print(machine.serve(t))
	machine.repair()
	print(machine.serve(t))
	print(machine.serve(t))