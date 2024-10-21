# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.index = 0
        self.flips = []
        
        def dfs(node):
            if not node:
                return True
            if node.val != voyage[self.index]:
                return False
            self.index += 1
            if node.left and node.left.val != voyage[self.index]:
                self.flips.append(node.val)
                return dfs(node.right) and dfs(node.left)
            return dfs(node.left) and dfs(node.right)
        
        if dfs(root):
            return self.flips
        return [-1]