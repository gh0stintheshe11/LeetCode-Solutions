# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorderTraversal(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)
        
        nums = inorderTraversal(root)
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        
        return False