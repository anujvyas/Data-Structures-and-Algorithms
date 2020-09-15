# Python program for implementation of Bubble sort

import time

def bubble_sort(a):
	for i in range(0, len(a)):

		# Last i elements are already sorted 
		for j in range(0, len(a)-1-i):
			
			# Swap if the element at j is greater than element j+1 index
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]




if __name__ == '__main__':

	a = [64, 12, 25, 12, 22, 11]
	print('Input: {}'.format(a))
	
	t0 = time.time()
	bubble_sort(a)
	t1 = time.time()

	print('Output: {}'.format(a))
	print('Execution time: {}'.format(t1-t0))