class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
	
def printLinkList(head):
	current = head
	while current is not None:
		
		if current.next is None:
			print(current.value)
			current = None
		else:
			print(f'{current.value} -> ', end = '') 
			current = current.next
			
node5 = Node('e', None)
node4 = Node('d', node5)
node3 = Node('c', node4)
node2 = Node('b', node3)
node1 = Node('a', node2)	




printLinkList(node1)