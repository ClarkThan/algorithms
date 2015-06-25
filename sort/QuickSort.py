#QuickSort
def middle(seq):
	length = len(seq)
	index = 0
	for i in xrange(1, length):
		if seq[i] < seq[index]:
			key = seq[i]
			j = i
			while j > index:
				seq[j] = seq[j-1]
				j = j - 1
			seq[index] = key
			index += 1
	return index
	
def quickSort(seq):
	if len(seq) <= 1:
		return seq
	mid = middle(seq)
	left = quickSort(seq[:mid])
	right = quickSort(seq[mid+1:])
	return left + [seq[mid]] + right
	
def quikcSort_v2(seq):
	return quikcSort_v2([x for x in seq[1:] if x <= seq[0]]) + [seq[0]] + quikcSort_v2([x for x in seq[1:] if x > seq[0]]) if seq else []

a = []
b = [-1]
c = [3, 2]
d = [11,-2,-5,21,10,3,7,33,0,13,3,5,-7,22,41,28,45]

if __name__ == '__main__':
	print quickSort(a)
	print quickSort(b)
	print quickSort(c)
	print quickSort(d)
	print quikcSort_v2(a)
	print quikcSort_v2(b)
	print quikcSort_v2(c)
	print quikcSort_v2(d)