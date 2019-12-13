def ReadFile(fileName):
	f = open('numbers.txt', 'r')
	f.close
	return (f.read())

def Number():
	nbr = ReadFile('numbers.txt')
	data = nbr.split(',')
	for i in range(len(data)):
		print(data[i])

if __name__ == '__main__':
	Number()