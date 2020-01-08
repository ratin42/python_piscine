import sys
import setting
import re

def createHtmlFile(FileContent, FileName):
	fd = open(FileName, "w+")
	fd.write(FileContent);

def render(fd):
	HtmlRender = fd.read()
	fd.close()
	Pattern = re.compile("\{(.*?)\}", re.S)
	Line = re.findall(Pattern, HtmlRender)
	for i in Line:
		if hasattr(setting, i):
			HtmlRender = re.sub("\{%s\}" % i, getattr(setting, i),HtmlRender)
	createHtmlFile(HtmlRender, 'file.html')

if __name__ == '__main__':
	if len(sys.argv) != 2:
		sys.exit(0)
	fd = open(sys.argv[1])
	render(fd)
