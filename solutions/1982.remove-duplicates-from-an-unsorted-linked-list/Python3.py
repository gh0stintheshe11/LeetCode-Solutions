# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        from collections import defaultdict
        
        # First pass to count all values
        count = defaultdict(int)
        current = head
        while current:
            count[current.val] += 1
            current = current.next
        
        # Second pass to remove values with duplicates
        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head
        while current:
            if count[current.val] > 1:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return dummy.next