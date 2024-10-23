
#node class
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def printlist(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next

def findfreq(head, val):
    current = head
    count = 0
    while current is not None:
        if current.value == val:
            count += 1
        current = current.next
    print(count)

# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    dummy = current.next

    while dummy.next is not None: 
        dummy = dummy.next
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return printlist(head)

list = Node(4, Node(3, Node(2, Node(4, None))))

#findfreq(list, 4)

remove_tail(list)