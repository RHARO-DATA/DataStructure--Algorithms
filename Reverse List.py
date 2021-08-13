"""
Reverse Linked List

Input:  1->2->3->4->5-> null
Output: 5->4->3->2->1-> null

"""
# Iterations

class Solution:
    def reverseList(self, head:ListNode)->ListNode:
        if head in None or if head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

#

class Solution:
    def reverseList(self, head:ListNode)->ListNode:
        prev = None
        curr = head
        while (curr != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev