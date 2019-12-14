d = {
	'Hendrix' : '1942',
	'Allman' : '1946',
	'King' : '1925',
	'Clapton' : '1945',
	'Johnson' : '1911',
	'Berry' : '1926',
	'Vaughan' : '1954',
	'Cooder' : '1947',
	'Page' : '1944',
	'Richards' : '1943',
	'Hammett' : '1962',
	'Cobain' : '1967',
	'Garcia' : '1942',
	'Beck' : '1944',
	'Santana' : '1947',
	'Ramone' : '1948',
	'White' : '1975',
	'Frusciante': '1970',
	'Thompson' : '1949',
	'Burton' : '1939',
}

def pSort(tab):
	i = len(tab) - 1
	while i > 0:
		j = 0
		while j < i - 1:
			if d[tab[j + 1]] == d[tab[j]] and tab[j + 1] < tab[j]:
				tab[j + 1], tab[j] = tab[j], tab[j + 1]
			j += 1
		i -= 1
	return tab

def mySort():
	keyList = list()
	YearSorted = dict()
	y = 0
	for i in sorted(d, key=d.get):
		keyList.append(i)
		y += 1
	keyList = pSort(keyList)
	for i in range(len(keyList)):
		print(keyList[i])

if __name__ == '__main__':
	mySort()