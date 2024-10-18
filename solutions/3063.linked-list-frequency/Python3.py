# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def frequenciesOfElements(self, head: ListNode) -> ListNode:
        from collections import defaultdict
        
        freq_map = defaultdict(int)
        
        current = head
        while current:
            freq_map[current.val] += 1
            current = current.next
        
        dummy_head = ListNode()
        current = dummy_head
        
        for key in freq_map:
            new_node = ListNode(freq_map[key])
            current.next = new_node
            current = current.next
        
        return dummy_head.next