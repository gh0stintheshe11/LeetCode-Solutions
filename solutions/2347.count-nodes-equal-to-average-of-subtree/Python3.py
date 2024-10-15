# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return (0, 0, 0)  # (sum, count, num_nodes_equal_to_average)

            left_sum, left_count, left_equal_count = dfs(node.left)
            right_sum, right_count, right_equal_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            
            # Check if current node value equals the average of its subtree
            is_avg_equal = node.val == total_sum // total_count

            equal_count = left_equal_count + right_equal_count + (1 if is_avg_equal else 0)

            return (total_sum, total_count, equal_count)

        _, _, result = dfs(root)
        return result