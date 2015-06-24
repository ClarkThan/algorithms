#SelectSort
def selectSort(seq):
	length = len(seq)
	for i in xrange(length-1):
		minIndex = i
		for j in xrange(i+1, length):
			if seq[j] < seq[minIndex]:
				minIndex = j
		seq[i], seq[minIndex] = seq[minIndex], seq[i]
	
	return seq
	
a = []
b = [-1]
c = [3, 2]
d = [11,-2,-5,21,10,3,7,33,0,13,5,-7,22,41,28,45]

if __name__ == '__main__':
	print selectSort(a)
	print selectSort(b)
	print selectSort(c)
	print selectSort(d)