class Elem:
	"""Html element Class"""

	def __init__(self, tag=None, attr=None, content=None, tag_type=None):
		if not isinstance(tag, str):
			self.tag = "div"
		else:
			self.tag = tag
			self.content = "<" + self.tag + ">" + "\n  " + "<div></div>" + "\n" + "</" + self.tag + ">"
		self.attr = attr
		self.content = content
		if not isinstance(content, str):
			self.content = "<" + self.tag + ">" + "</" + self.tag + ">"
		self.type = tag_type
		print("content = %s" % self.content)

	def __str__(self):
		return self.content
	
	def add_content(self):
		print(self.tag)
		print(self.attr)
		print(self.content)
		print(self.type)

class Text(str):

	def __init__(self, content= ""):
		self.str = content
		if "<" in self.str:
			self.str = self.str.replace("<", "&lt;", -1)
		if ">" in self.str:
			self.str = self.str.replace(">", "&gt;", -1)
		if "\"" in self.str:
			self.str = self.str.replace("\"", "&quot;", -1)
		if "\n" in self.str:
			self.str = self.str.replace("\n", "\n<br />\n", -1)

	def __str__(self):
	 return self.str

if __name__ == "__main__":
	e = Elem("p", None, content="Oh no, not again!", tag_type="double")
	#e.add_content()