# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find length of list
        n = 0
        current = head
        while current:
            n += 1
            current = current.next
        
        # Find k-th node from beginning and end
        first_kth = last_kth = head
        for _ in range(k - 1):
            first_kth = first_kth.next
        for _ in range(n - k):
            last_kth = last_kth.next
        
        # Swap values of the k-th nodes
        first_kth.val, last_kth.val = last_kth.val, first_kth.val
        
        return head