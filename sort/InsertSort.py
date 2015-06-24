#InsertSort
def insertSort(seq):
	length = len(seq)
	for i in xrange(1, length):
		key = seq[i]
		j = i - 1
		while j >= 0 and seq[j] > key:
			seq[j+1] = seq[j]
			j = j - 1
		seq[j+1] = key
		
	return seq
	
a = []
b = [-1]
c = [3, 3]
d = [11,-2,-5,21,10,3,7,33,0,13,5,-7,22,41,28,45]

if __name__ == '__main__':
	print insertSort(a)
	print insertSort(b)
	print insertSort(c)
	print insertSort(d)
