# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def toArray(self, root: 'Node') -> List[int]:
        result = []
        current = root
        while current:
            result.append(current.val)
            current = current.next
        return result