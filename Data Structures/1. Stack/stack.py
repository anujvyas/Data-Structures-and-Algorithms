# Data Structure: Stack
# Implemented by: List
# Methods: push, pop, peek, is_empty, get_stack

class Stack():

	def __init__(self):
		self.items = list()

	def push(self, element):
		self.items.append(element)

	def pop(self):
		if self.is_empty():
			return 'Cannot perform pop, stack is empty!'
		else:
			return self.items.pop()

	def peek(self):
		if self.is_empty():
			return 'Cannot perform peek, stack is empty!'
		else:
			return self.items[-1]

	def is_empty(self):
		return self.items == []

	def get_stack(self):
		return self.items




if __name__ == '__main__':

	s = Stack()
	s.push('A')
	s.push('B')
	print('stack: {}'.format(s.get_stack()))
	s.push('C')
	print('stack: {}'.format(s.get_stack()))
	s.pop()
	s.pop()
	print('stack: {}'.format(s.get_stack()))
	if s.is_empty():
		print('The stack is empty!')
	else:
		print('The stack has elements.')
	print('Element on top of the stack: {}'.format(s.peek()))
	s.pop()
	print('Element on top of the stack: {}'.format(s.peek()))
