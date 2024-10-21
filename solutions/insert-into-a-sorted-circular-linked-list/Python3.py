# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        
        # If the list is empty, create a new single node circular list.
        if not head:
            new_node.next = new_node
            return new_node
        
        prev, curr = head, head.next
        while True:
            # Case 1: insert between two nodes
            if prev.val <= insertVal <= curr.val:
                prev.next = new_node
                new_node.next = curr
                return head
            # Case 2: insert at the boundary, biggest or smallest position
            if prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    prev.next = new_node
                    new_node.next = curr
                    return head
            
            prev, curr = curr, curr.next
            # If we looped through list entirely and found no place
            if prev == head:
                break
        
        # Case 3: all nodes have the same value or we came full circle without finding position
        prev.next = new_node
        new_node.next = curr
        return head