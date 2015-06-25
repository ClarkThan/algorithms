#MergeSort
def merge(left, right):
	merged = []
	while left and right:
		merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
	while left:
		merged.append(left.pop(0))
	while right:
		merged.append(right.pop(0))	
	return merged
	
def mergeSort(seq):
	length = len(seq)
	if length <= 1:
		return seq
	middle = length / 2
	left = mergeSort(seq[:middle])
	right = mergeSort(seq[middle:])
	return merge(left, right)

a = []
b = [-1]
c = [3, 2]
d = [11,-2,-5,21,10,3,7,33,0,13,5,3,-7,22,41,28,45]

if __name__ == '__main__':
	print mergeSort(a)
	print mergeSort(b)
	print mergeSort(c)
	print mergeSort(d)