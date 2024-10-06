# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return [0] * (distance + 1)
            
            if not node.left and not node.right:
                leaves = [0] * (distance + 1)
                leaves[1] = 1
                return leaves
            
            left_leaves = dfs(node.left)
            right_leaves = dfs(node.right)
            
            for l in range(1, distance):
                for r in range(1, distance - l + 1):
                    self.count += left_leaves[l] * right_leaves[r]
            
            new_leaves = [0] * (distance + 1)
            for i in range(1, distance):
                new_leaves[i + 1] = left_leaves[i] + right_leaves[i]
            
            return new_leaves
        
        self.count = 0
        dfs(root)
        return self.count