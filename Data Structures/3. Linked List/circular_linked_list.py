# Data Structure: Circular LinkedList
# Methods: 	1. traverse
# 			2. insertion:
# 				• append_node
# 				• prepend_node
# 			3. deletion:
# 				• delete_node

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class CircularLL:
	def __init__(self):
		self.head = None


	# ------------- Traversal --------------
	def traverse(self):
		# If linkedlist is empty
		if self.head == None:
			print('Cannot traverse as linkedlist is empty!')
			return -1

		# If linkedlist has nodes
		temp = self.head
		while temp.next != self.head:
			print('{} -> '.format(temp.data), end='')
			temp = temp.next
		print('{} -> (Head)'.format(temp.data))


	# ------------- Insertion --------------
	def append_node(self, data):

		# If linkedlist is empty
		if self.head == None:
			self.head = Node(data)
			self.head.next = self.head
			return -1

		# Find the node who's next field is pointing to head
		new_node = Node(data)
		curr = self.head
		while curr.next != self.head:
			curr = curr.next
		curr.next = new_node
		new_node.next = self.head
		return -1

	def prepend_node(self, data):

		# If linkedlist is empty
		if self.head == None:
			self.head = Node(data)
			self.head.next = self.head
			return -1

		# Find the node who's next field is pointing to head
		new_node = Node(data)
		last = self.head
		while last.next != self.head:
			last = last.next
		new_node.next = self.head
		self.head = new_node
		last.next = self.head
		return -1


	# ------------- Deletion --------------
	def delete_node(self, data):
		# If linkedlist is empty
		if self.head == None:
			print('Cannot delete node "{}" as linkedlist is empty!'.format(data))
			return -1

		# If linkedlist has only one node
		if self.head.next == self.head and self.head.data == data:
			self.head = None
			return -1

		# Search for matching value
		temp = self.head
		behind_temp = None
		while temp.next != self.head:

			if temp.data == data:
				# If data is at head
				if temp == self.head:
					# Find the last node
					last = self.head
					while last.next != self.head:
						last = last.next

					self.head = self.head.next
					last.next = self.head


				# If data is not at head
				else:
					behind_temp.next = temp.next
				return -1
			
			behind_temp = temp
			temp = temp.next

		# If last node has matching value
		if temp.data == data:
			if behind_temp == None:
				self.head = None 
			else:
				behind_temp.next = temp.next





if __name__ == '__main__':

	l = CircularLL()

	l.append_node("A")
	l.append_node("B")
	l.append_node("C")
	l.append_node("D")
	l.traverse()

	l.prepend_node("Z")
	l.traverse()

	l.delete_node("D")
	l.traverse()
