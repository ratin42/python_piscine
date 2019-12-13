def MyVar():
	Nbr = 42
	NbrStr = "42"
	NbrStrChar = "quarante-deux"
	NbrFloat = 42.0
	VarBool = True
	VarList = [42]
	VarDict = {
		42 : 42
	}
	VarTuple = (42,)
	VarSet = set()
	print("%d est de type %s" % (Nbr, type(Nbr)))
	print("%s est de type %s" % (NbrStr, type(NbrStr)))
	print("%s est de type %s" % (NbrStrChar, type(NbrStrChar)))
	print("%.1f est de type %s" % (NbrFloat, type(NbrFloat)))
	print("%r est de type %s" % (VarBool, type(VarBool)))
	print("%r est de type %s" % (VarList, type(VarList)))
	print("%r est de type %s" % (VarDict, type(VarDict)))
	print("%r est de type %s" % (VarTuple, type(VarTuple)))
	print("%r est de type %s" % (VarSet, type(VarSet)))


if __name__ == '__main__':
	MyVar()
