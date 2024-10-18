# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        current = head
        
        while current:
            # keep m nodes
            for _ in range(1, m):
                if not current:
                    return head
                current = current.next
            
            # delete n nodes
            temp = current.next if current else None
            for _ in range(n):
                if not temp:
                    break
                temp = temp.next
            
            if current:
                current.next = temp
                current = temp
        
        return head