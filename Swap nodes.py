"""

 Swap every two nodes in a linked list
Given a linked list, swap the posicion of the 1st and 2nd node, then swap the posicion of the 3rd.


"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"

def swap_every_two(llist):
    head = llist
    curr = head
    while curr is not None and curr.next is not None:
        curr.value,curr.next.value = curr.next.value, curr.value
        curr = curr.next.next
    
    return head

llist =Node(1, Node(2, Node(3, Node(4, Node (5)))))    
llist =Node(2, Node(1, Node(4, Node(3, Node (5))))) 

print(swap_every_two(llist))
