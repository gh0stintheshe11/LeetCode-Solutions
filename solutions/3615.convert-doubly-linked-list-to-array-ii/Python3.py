# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        # Move to the head of the doubly linked list
        while node.prev:
            node = node.prev

        # Collect the elements in order
        result = []
        while node:
            result.append(node.val)
            node = node.next

        return result