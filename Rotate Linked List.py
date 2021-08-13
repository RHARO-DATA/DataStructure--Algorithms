"""
Rotate Linked List

Given  a Linked List and a number k, rotate the linked list by k places.

"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        curr = self
        ret = ''
        while curr:
            ret += str(curr.value) + "->"
            curr = curr.next
        return ret

def rotate_list(list, k):
    lenght = 0
    curr = list
    while curr:
        lenght += 1
        curr = curr.next

    k = k % lenght

    fast, slow = list, list

    for _ in range(k):
        fast = fast.next

    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    fast.next = list
    head = slow.next
    slow.next = None
    
    return head


llist = Node(1, Node(2,Node(3, Node(4))))


print(rotate_list(llist,2))