from math import gcd
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            next_node = current.next
            g = gcd(current.val, next_node.val)
            new_node = ListNode(g, next_node)
            current.next = new_node
            current = next_node
        return head