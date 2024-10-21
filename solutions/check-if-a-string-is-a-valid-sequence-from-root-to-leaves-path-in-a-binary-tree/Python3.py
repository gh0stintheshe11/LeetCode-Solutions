# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(node, index):
            if node is None:
                return False
            if index >= len(arr):
                return False
            if node.val != arr[index]:
                return False
            if index == len(arr) - 1:
                return node.left is None and node.right is None
            return dfs(node.left, index + 1) or dfs(node.right, index + 1)
        
        return dfs(root, 0)