# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        def findClosestElements(arr, k, x):
            left, right = 0, len(arr) - k
            while left < right:
                mid = (left + right) // 2
                if x - arr[mid] > arr[mid + k] - x:
                    left = mid + 1
                else:
                    right = mid
            return arr[left:left + k]
        
        values = inorder(root)
        return findClosestElements(values, k, target)