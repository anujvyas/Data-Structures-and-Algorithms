# Swap two nodes in a given linkedlist without swapping data

from singly_linked_list import  Node, LinkedList

def swap_node(head, x, y):
	# If both values are same
	if x == y:
		return head

	# Find x
	prevX = None
	currX = head

	while currX != None and currX.data != x:
		prevX = currX
		currX = currX.next

	# Find y
	prevY = None
	currY = head

	while currY != None and currY.data != y:
		prevY = currY
		currY = currY.next

	# If any of the value is not present in the linkedlist
	if currX == None or currY == None:
		print('Cannot swap nodes as one or more nodes not present in linkedlist!')
		return head

	# If x is head // make y as the new head
	if prevX == None:
		head = currY
	else:
		prevX.next = currY

	# If y is head // make x as the new head
	if prevY == None:
		head = currX
	else:
		prevY.next = currX
		
	# Swap next pointers
	temp = currX.next
	currX.next = currY.next
	currY.next = temp

	return head	







if __name__ == '__main__':

	l = LinkedList()

	l.append_node("A")
	l.append_node("B")
	l.append_node("C")
	l.append_node("D")

	l.traverse()
	l.head = swap_node(l.head, 'A', 'C')
	l.traverse()