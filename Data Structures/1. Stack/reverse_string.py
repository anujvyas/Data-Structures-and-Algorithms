# Use a stack data structure to reverse any given string.

# Example: Hello -> olleH

from stack import Stack

def reverse_string(inString):
	
	if len(inString) == 1:
		return inString

	s = Stack()
	
	for index in range(0, len(inString)):
		alphabet = inString[index]
		s.push(alphabet)

	revString = ''
	while not s.is_empty():
		revString = revString + s.pop()

	return revString





if __name__ == '__main__':
	print('The reverse of "Hello" is: {}'.format(reverse_string('Hello')))
	print('The reverse of "World" is: {}'.format(reverse_string('World')))