# Use a stack to check whether or not a string has balanced usage of parenthesis.

# Example:
#     (), ()(), (({[]}))  <- Balanced.
#     ((), {{{)}], [][]]] <- Not Balanced.

# Balanced Example: {[]}
# Non-Balanced Example: (()
# Non-Balanced Example: ))

from stack import Stack

def is_matching_set(open, close):
	if (open == '(' and close == ')') or (open == '[' and close == ']') or (open == '{' and close == '}'):
		return True

	return False


def is_balanced(paraString):
	s = Stack()
	index = 0

	while index < len(paraString):
		element = paraString[index]
		
		# If found opening parenthesis
		if element in '([{':
			s.push(element)

		# Else found closing parenthesis
		else:

			# If stack is empty
			if s.is_empty():
				return False

			# If top of stack is equal to closing parenthesis
			elif is_matching_set(s.peek(), element):
				s.pop()
			
			# Else mismatch
			else:
				return False

		index = index + 1

	# If no parenthesis found in stack
	if s.is_empty():
		return True
	# If found any opening parenthesis remaining in stack
	else:
		return False





if __name__ == '__main__':
	
	if is_balanced("((()))"):
		print('Parenthesis are balanced!')
	else:
		print('Parenthesis are not balanced.')

	if is_balanced("]}][{"):
		print('Parenthesis are balanced!')
	else:
		print('Parenthesis are not balanced.')

	if is_balanced("(()"):
		print('Parenthesis are balanced!')
	else:
		print('Parenthesis are not balanced.')