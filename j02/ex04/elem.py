class Elem:
	"""Html element Class"""

	def __init__(self, tag=None, attr=None, content=None, tag_type=None):
		if content == "" and not isinstance(content, Text):
			raise self.ValidationError()

		self.attr = attr

		if tag == None or tag == "":
			self.tag = "div"
		else:
			self.tag = tag

		self.in_tag_o = "<" + self.tag + ">"
		self.in_tag_c = "</" + self.tag + ">"

		if tag_type == None:
			self.type = "double"
		else:
			self.type = tag_type
		
		self.get_content(content)
		#print("#%s\n------------------------\n" % repr(self.content))


	def get_content(self, content):
		if content == None or content == "" or (isinstance(content, list) and len(set(content))==1 and content[0] == ""):
			if self.type is "double":
				self.content = self.in_tag_o + self.in_tag_c
			else:
				self.content = self.in_tag_o
		else:
			if isinstance(content, list):
				self.content = self.in_tag_o + "\n" + self.get_list(content) + self.in_tag_c
			else:
				self.content = self.in_tag_o + "\n" + str(content) + "\n" + self.in_tag_c
		self.do_indent()

	def do_indent(self):
		count_open = 0
		self.content = self.content.replace(" ", "")
		elem = self.content.split("\n")
		self.content = ""
		for i in elem:
			if "<" in i and "/" in i.split(">")[0]:
				count_open -= 1
			for x in range(0, count_open):
				i = "  " + i
			if "<" in i and "/" not in i:
				count_open += 1
			if i != elem[-1]:
				i += "\n"
			self.content += i
		
	
	def get_list(self, content):
		list_content = ""
		for i in content:
			if i != "" and i != None:
				list_content = list_content + "  " + str(i) + "\n"
		return list_content

	def __str__(self):
		return str(self.content)

	def add_content(self, content):
		raise self.ValidationError()

	class ValidationError(Exception):
		pass

class Text(str):

	def __init__(self, content= ""):
		self.str = str(content)
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
	e = Elem(content='')
	print("\n$$$$$$$$$$$$$$$$$$$$$$$$$\n")
	print(e)