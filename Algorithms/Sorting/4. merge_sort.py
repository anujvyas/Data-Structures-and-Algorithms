# Python program for implementation of Merge sort

import time


def merge(x, y, subarray):
	
	index = 0	
	x_index = 0
	y_index = 0

	while x_index<len(x) and y_index<len(y):
		if x[x_index] <= y[y_index]:
			subarray[index] = x[x_index]
			x_index += 1
		else:
			subarray[index] = y[y_index]
			y_index += 1
		index += 1

	# If x gets empty
	while y_index<len(y):
		subarray[index] = y[y_index]
		y_index += 1
		index += 1

	# If y gets empty
	while x_index<len(x):
		subarray[index] = x[x_index]
		x_index += 1
		index += 1


def merge_sort(a):

	if len(a) >= 2:
		mid = len(a)//2
		left_subarray = a[:mid]
		right_subarray = a[mid:]

		# Recursive calls
		merge_sort(left_subarray)
		merge_sort(right_subarray)
		merge(left_subarray, right_subarray, a)







if __name__ == '__main__':

	a = [64, 12, 25, 12, 22, 11]
	print('Input: {}'.format(a))
	
	t0 = time.time()
	merge_sort(a)
	t1 = time.time()

	print('Output: {}'.format(a))
	print('Execution time: {}'.format(t1-t0))