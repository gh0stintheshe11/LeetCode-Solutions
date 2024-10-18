# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        # Helper function to reverse the linked list
        def reverse(node: ListNode) -> ListNode:
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        
        # Reverse the original list
        head = reverse(head)
        
        # Process the reversed list to remove nodes
        max_val = float('-inf')
        prev_node = None
        current = head
        
        while current:
            if current.val >= max_val:
                max_val = current.val
                prev_node = current
                current = current.next
            else:
                prev_node.next = current.next
                current = current.next
        
        # Reverse the list again to get the desired result
        return reverse(head)