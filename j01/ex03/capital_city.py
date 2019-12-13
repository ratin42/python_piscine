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

def CapitalCity():
	if (len(sys.argv) != 2):
		sys.exit(0)
	stateName = sys.argv[1].title()
	if stateName in states:
		print(capital_cities[states[stateName]])
	else:
		print('Unknown state')

if __name__ == '__main__':
	CapitalCity()