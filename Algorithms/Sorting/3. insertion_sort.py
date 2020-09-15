# Python program for implementation of Insertion sort

# Input = [64, 12, 25, 12, 22, 11]
# Step 1. [12, 64, 25, 12, 22, 11]
# Step 2. [12, 25, 64, 12, 22, 11]
# Step 3. [12, 12, 25, 64, 22, 11]
# Step 4. [12, 12, 22, 25, 64, 11]
# Step 5. [11, 12, 12, 22, 25, 64] = Output

import time

def insertion_sort(a):

	for index in range(1, len(a)):
		
		value = a[index]
		j = index-1

		while j>=0 and value<a[j]:
			# Shift to right by 1 unit
			a[j+1] = a[j]
			j -= 1
		a[j+1] = value




if __name__ == '__main__':

	a = [64, 12, 25, 12, 22, 11]
	print('Input: {}'.format(a))

	t0 = time.time()
	insertion_sort(a)
	t1 = time.time()

	print('Output: {}'.format(a))
	print('Execution time: {}'.format(t1-t0))