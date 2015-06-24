#BubbleSort
def bubbleSort(seq):
	length = len(seq)
	for i in xrange(length):
		for j in xrange(1,length-i):
			if seq[j-1] > seq[j]:
				seq[j-1], seq[j] = seq[j], seq[j-1]
	
	return seq

a = []
b = [-1]
c = [3, 2]
d = [11,-2,-5,21,10,3,7,33,0,13,5,-7,22,41,28,45]

if __name__ == '__main__':
	print bubbleSort(a)
	print bubbleSort(b)
	print bubbleSort(c)
	print bubbleSort(d)