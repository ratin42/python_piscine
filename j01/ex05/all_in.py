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

def GetCapitalName(stateName):
    if stateName in states:
        return capital_cities[states[stateName]]
    else:
        return (0)
    
def GetStateName(capitalName):
    if capitalName in list(capital_cities.values()):
        code = list(capital_cities.keys())[list(capital_cities.values()).index(capitalName)]
        return (list(states.keys())[list(states.values()).index(code)])
    else:
        return (0)

def allin():
    if (len(sys.argv) != 2):
        sys.exit(0)
    toSearch = sys.argv[1].split(',')
    for i in range(len(toSearch)):
        toCheck = toSearch[i].lstrip().lower().title()
        matchCapital = GetCapitalName(toCheck)
        if toCheck:
            if matchCapital:
                print("%s is the capital of %s" % (matchCapital, toCheck))
            matchState = GetStateName(toCheck)
            if matchState:
                print("%s is the capital of %s" % (toCheck, matchState))
            if matchCapital == 0 and matchState == 0:
                print("%s is neither a capital city nor a state" % (toCheck))

if __name__ == '__main__':
    allin()
