# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.cameras = 0
        
        def dfs(node):
            if not node:
                return 2  # Null nodes are considered covered
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == 0 or right == 0:
                # If any child needs to be monitored, place a camera here
                self.cameras += 1
                return 1  # This node has a camera
            
            if left == 1 or right == 1:
                # If any child has a camera, this node is covered
                return 2  # This node is covered
            
            # If children are covered but do not have a camera, this node needs to be monitored
            return 0
        
        # If the root itself needs to be monitored, place a camera
        if dfs(root) == 0:
            self.cameras += 1
        
        return self.cameras
