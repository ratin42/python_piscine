import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}

capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

def state():
	if (len(sys.argv) != 2):
		sys.exit(0)
	capitalName = sys.argv[1].title()
	if capitalName in list(capital_cities.values()):
		code = list(capital_cities.keys())[list(capital_cities.values()).index(capitalName)]
	    print(list(states.keys())[list(states.values()).index(code)])
	else:
		print('Unknown capital city')
		sys.exit(0)

if __name__ == '__main__':
	state()