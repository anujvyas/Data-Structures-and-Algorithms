# Reverse a given linkedlist

from singly_linked_list import Node, LinkedList


def reverseLinkedList(head):
	# If linkedlist is empty
	if head == None:
		print('Cannot perform operation as linkedlist is empty!')
		return head

	# If linkedlist has only one node
	if head.next == None:
		return head

	# If linkedlist has more than one nodes
	front = head.next.next
	back = head
	head = head.next
	back.next = None
	
	while front != None:
		head.next = back
		back = head
		head = front
		front = front.next

	head.next = back
	return head





if __name__ == '__main__':
	l = LinkedList()

	l.append_node("A")
	l.append_node("B")
	l.append_node("C")

	l.traverse()
	l.head = reverseLinkedList(l.head)
	l.traverse()