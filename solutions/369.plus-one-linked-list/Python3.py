# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # Reverse the linked list
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        reversed_head = prev

        # Add one to the number
        current = reversed_head
        carry = 1
        while current:
            current.val += carry
            if current.val == 10:
                current.val = 0
                carry = 1
            else:
                carry = 0
            if carry == 0:
                break
            if current.next is None:
                current.next = ListNode(0)
            current = current.next

        # Reverse the linked list again
        prev = None
        current = reversed_head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev