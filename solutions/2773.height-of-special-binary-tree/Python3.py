# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def heightOfTree(self, root: Optional[TreeNode]) -> int:
        def traverse(testroot: Optional[TreeNode], level: int) -> int:
            if testroot is not None:
                if testroot.left is not None and testroot.left.right == testroot:
                    return level
                elif testroot.right is not None and testroot.right.left == testroot:
                    return level
                else:
                    return max(traverse(testroot.left, level + 1), traverse(testroot.right, level + 1))
                
            else:
                return 0
            
        return traverse(root, 0)