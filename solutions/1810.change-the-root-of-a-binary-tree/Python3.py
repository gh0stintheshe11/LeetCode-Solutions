# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        current = leaf
        parent = leaf.parent
        leaf.parent = None
        
        while parent is not None:
            # Store the parent's parent (to move up the tree)
            next_parent = parent.parent
            
            # If current node has a left child, it should become the right child.
            if current.left:
                current.right = current.left
            
            # Make the parent the left child of current
            current.left = parent
            
            # Break the link in the original tree
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            
            # Update the parent link
            parent.parent = current
            current = parent
            parent = next_parent
        
        return leaf