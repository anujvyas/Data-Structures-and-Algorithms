# Use a stack data structure to convert integer values to their corresponding binary representation.

# Example : 242
# 242 / 2 = 121 -> 0
# 121 / 2 = 60  -> 1
# 60 / 2  = 30  -> 0
# 30 / 2  = 15  -> 0
# 15 / 2  = 7   -> 1
# 7 / 2 = 3     -> 1
# 3 / 2 = 1     -> 1
# 1 / 2 = 0	  -> 1

from stack import Stack

def int_to_bin(number):
	
	if number == 0:
		return 0
	elif number == 1:
		return 1

	s = Stack()
	remainder = 0
	
	while number > 1:
		remainder = number % 2
		s.push(remainder)
		number = number//2
	s.push(remainder)

	binary = ''
	while not s.is_empty():
		binary = binary + str(s.pop())

	return int(binary)





if __name__ == '__main__':
	print('The binary equivalent of 242 is: {}'.format(int_to_bin(242)))
	print('The binary equivalent of 198 is: {}'.format(int_to_bin(198)))