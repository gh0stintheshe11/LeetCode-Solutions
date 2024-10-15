# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the (a-1)th node
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next
        
        # Find the (b+1)th node
        after_b = prev_a
        for _ in range(b - a + 2):
            after_b = after_b.next
        
        # Connect the (a-1)th node to the head of list2
        prev_a.next = list2
        
        # Go to the end of list2
        last_list2 = list2
        while last_list2.next:
            last_list2 = last_list2.next
        
        # Connect the last node of list2 to the (b+1)th node of list1
        last_list2.next = after_b
        
        return list1