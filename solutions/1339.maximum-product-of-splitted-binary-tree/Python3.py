# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        
        # Helper function to calculate the total sum of the tree
        def get_total_sum(node):
            if not node:
                return 0
            return node.val + get_total_sum(node.left) + get_total_sum(node.right)
        
        # Calculate the total sum of the tree
        total_sum = get_total_sum(root)
        
        # Variable to store the maximum product
        self.max_product = 0
        
        # Helper function to calculate subtree sums and update max_product
        def calculate_subtree_sum(node):
            if not node:
                return 0
            # Calculate the sum of the current subtree
            subtree_sum = node.val + calculate_subtree_sum(node.left) + calculate_subtree_sum(node.right)
            # Calculate the product of the current split
            product = subtree_sum * (total_sum - subtree_sum)
            # Update the maximum product
            self.max_product = max(self.max_product, product)
            return subtree_sum
        
        # Calculate subtree sums and update max_product
        calculate_subtree_sum(root)
        
        # Return the result modulo 10^9 + 7
        return self.max_product % MOD
