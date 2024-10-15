# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        from collections import defaultdict
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            count[node.val] += 1
            inorder(node.right)
        
        count = defaultdict(int)
        inorder(root)
        
        max_count = max(count.values())
        return [k for k, v in count.items() if v == max_count]