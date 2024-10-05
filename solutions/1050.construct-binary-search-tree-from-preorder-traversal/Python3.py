# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        
        for value in preorder[1:]:
            node, child = stack[-1], TreeNode(value)
            
            # Adjust the stack and insert the child in the correct position
            while stack and stack[-1].val < value:
                node = stack.pop()
                
            if value < node.val:
                node.left = child
            else:
                node.right = child
                
            stack.append(child)
        
        return root