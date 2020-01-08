class Intern():
	"""intern class"""

	def __init__(self, Name="My name? I’m nobody, an intern, I have no name." ):
	 super().__init__()
	 self.name = Name

	def __str__(self):
	 return self.name

	def Work(self):
		raise Exception("I’m just an intern, I can’t do that...")

	def MakeCoffee(self):
		return Intern.Coffee()

	class Coffee():
		"""Making coffee class"""

		def __str__(self):
			return "This is the worst coffee you ever tasted."
	
if __name__ == '__main__':
	ratin = Intern()
	print(ratin, ratin.MakeCoffee())
	try:
		ratin.Work()
	except Exception:
		print("Exception when asked to work")