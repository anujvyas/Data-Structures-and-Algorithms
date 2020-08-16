# Data Structure: LinkedList
# Methods: 	1. traverse
# 			2. insertion:
# 				• append_node
# 				• prepend_node
# 				• insert_node_after
# 			3. deletion:
# 				• delete_node
# 				• delete_node_at_position




class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None


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

	# -------------- Insertion --------------
	def append_node(self, data):
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

	def prepend_node(self, data):
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



	# -------------- Deletion --------------
	def delete_node(self, data):
		# If linkedlist is empty
		if self.head == None:
			print('Cannot delete node "{}" as linkedlist is empty!'.format(data))
			return -1

		# Search for matching value
		temp = self.head
		behind_temp = self.head
		while temp.next != None:
			# If found the data
			if temp.data == data:
				
				# If data is at head
				if temp == self.head:
					self.head = self.head.next

				# If data is not at head
				else:
					behind_temp.next = temp.next
				return -1
			
			# If first iteration
			if temp != behind_temp:
				behind_temp = temp

			temp = temp.next

		# If last node has matching value
		if temp.data == data:
			behind_temp.next = temp.next
			return -1
		
		# If value not found in linkedlist
		else:
			print('Cannot delete node "{}" as value not found in linkedlist!'.format(data))

	def delete_node_at_position(self, position):
		# If linkedlist is empty
		if self.head == None:
			print('Cannot delete node at position "{}" as linkedlist is empty!'.format(position))
			return -1

		if position == 0:
			self.head = self.head.next
			return -1

		temp = self.head
		current_position = 0
		flag = -1

		while temp.next != None:
			if position == current_position:
				flag = 1
				break 

			temp = temp.next
			current_position += 1

		# If found element or last node is at the given position
		if flag == 1 or position == current_position:
			temp1 = self.head

			# Find temp
			while temp1.next != temp:
				temp1 = temp1.next

			# Skip the temp node
			temp1.next = temp1.next.next
			return -1

		# If position not found in linkedlist
		else:
			print('Cannot delete node at position "{}" as position > len(linkedlist)'.format(position))



if __name__ == '__main__':
	l = LinkedList()

	# -------------- Insertion --------------
	l.append_node("C")
	l.append_node("D")
	l.traverse()

	l.prepend_node("B")
	l.prepend_node("A")
	l.traverse()

	l.insert_node_after("D", "E")
	l.traverse()

	l.insert_node_after("Z", "E")
	l.traverse()

	# -------------- Deletion --------------
	l.delete_node("D")
	l.traverse()

	l.delete_node("A")
	l.traverse()

	l.delete_node_at_position(1)
	l.traverse()