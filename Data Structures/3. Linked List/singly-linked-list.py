# Data Structure: LinkedList
# Methods: append, prepend, insert_node_after, traverse

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)

		# If linkedlist is empty
		if self.head == None:
			self.head = new_node
			return -1

		# If linkedlist has nodes
		temp = self.head
		while temp.next != None:
			temp = temp.next
		temp.next = new_node

	def prepend(self, data):
		new_node = Node(data)

		# If linkedlist is empty or not empty
		new_node.next = self.head
		self.head = new_node

	def insert_node_after(self, prev_data, data):
		
		# If linkedlist is empty
		if self.head == None:
			print('Cannot insert node after "{}" as linkedlist is empty!'.format(prev_data))
			return -1

		# Search for matching value in all nodes except last
		temp = self.head
		while temp.next != None:
			if temp.data == prev_data:
				new_node = Node(data)
				new_node.next = temp.next
				temp.next = new_node
				return -1
			temp = temp.next

		# If last node has matching value
		if temp.data == prev_data:
			new_node = Node(data)
			new_node.next = temp.next
			temp.next = new_node
			return -1
		
		# If value not found in linkedlist
		else:
			print('Cannot insert node after "{}" as value not found in linkedlist!'.format(prev_data))

	def traverse(self):
		# If linkedlist is empty
		if self.head == None:
			print('Cannot traverse as linkedlist is empty!')

		# If linkedlist has nodes
		temp = self.head
		# Print values of all nodes except last
		while temp.next != None:
			print('{} -> '.format(temp.data), end='')
			temp = temp.next
		# Print value of last node
		print('{} -> NULL'.format(temp.data))





if __name__ == '__main__':
	l = LinkedList()

	l.append("C")
	l.append("D")
	l.traverse()

	l.prepend("B")
	l.prepend("A")
	l.traverse()

	l.insert_node_after("D", "E")
	l.traverse()

	l.insert_node_after("Z", "E")