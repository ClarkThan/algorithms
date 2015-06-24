#ShellSort
import math

def shellSort(seq):
	length = len(seq)
	step = int(math.ceil(math.sqrt(length)))
	while step:
		for i in xrange(step, length):
			key = seq[i]
			j = i - step
			while j >=0 and seq[j] > key:
				seq[j+step] = seq[j]
				j = j - step
			seq[j+step] = key
		step = step / 2
	
	return seq

a = []
b = [-1]
c = [3, 2]
d = [11,-2,-5,21,10,3,7,33,0,13,5,-7,22,41,28,45]

if __name__ == '__main__':
	print shellSort(a)
	print shellSort(b)
	print shellSort(c)
	print shellSort(d)