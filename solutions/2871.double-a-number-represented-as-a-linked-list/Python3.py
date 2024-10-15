# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = None
        current = head
        carry = 0
        
        # Reverse the linked list
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        head = prev
        current = head
        
        # Traverse reversed list and double the value
        while current:
            current.val = current.val * 2 + carry
            carry = current.val // 10
            current.val = current.val % 10
            prev = current
            current = current.next
        
        # If we have a carry after the last digit
        if carry > 0:
            prev.next = ListNode(carry)
        
        # Reverse the list back to original order
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev