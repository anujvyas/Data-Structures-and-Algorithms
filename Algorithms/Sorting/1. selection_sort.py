# Python program for implementation of Selection sort

# Input = [64, 12, 25, 12, 22, 11]
# Step 1. [11, 12, 25, 12, 22, 64]
# Step 2. [11, 12, 25, 12, 22, 64]
# Step 3. [11, 12, 12, 25, 22, 64]
# Step 4. [11, 12, 12, 22, 25, 64]
# Step 5. [11, 12, 12, 22, 25, 64] = Output

import time

def selection_sort(a):
	for index in range(0, len(a)-1):

		# Find index of minimum element in the array from index till end
		min_index = index
		for j in range(index+1, len(a)):
			if a[min_index] > a[j]:
				min_index = j

		# Swap the found minimum element with index element
		a[index], a[min_index] = a[min_index], a[index]




if __name__ == '__main__':

	a = [64, 12, 25, 12, 22, 11]
	print('Input: {}'.format(a))
	
	t0 = time.time()
	selection_sort(a)
	t1 = time.time()

	print('Output: {}'.format(a))
	print('Execution time: {}'.format(t1-t0))