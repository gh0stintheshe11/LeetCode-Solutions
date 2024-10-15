# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum = 0
        
        def postorder(node):
            if not node:
                return (0, True, float('-inf'), float('inf'))
            
            left_sum, is_left_bst, left_max, left_min = postorder(node.left)
            right_sum, is_right_bst, right_max, right_min = postorder(node.right)
            
            if is_left_bst and is_right_bst and left_max < node.val < right_min:
                current_sum = node.val + left_sum + right_sum
                self.maxSum = max(self.maxSum, current_sum)
                
                current_max = max(node.val, right_max)
                current_min = min(node.val, left_min)
                
                return (current_sum, True, current_max, current_min)
            else:
                return (0, False, 0, 0)
        
        postorder(root)
        return self.maxSum