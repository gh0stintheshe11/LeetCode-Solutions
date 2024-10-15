# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        queue = deque([(root, None)])
        visited = set()

        while queue:
            next_level = deque()
            
            while queue:
                node, parent = queue.popleft()

                if node.right:
                    if node.right.val in visited:
                        if parent.left == node:
                            parent.left = None
                        else:
                            parent.right = None
                        return root
                    next_level.append((node.right, node))
                
                if node.left:
                    next_level.append((node.left, node))
                
                visited.add(node.val)

            queue = next_level
        
        return root