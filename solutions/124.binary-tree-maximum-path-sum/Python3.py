class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.max_gain(root)
        return self.max_sum
    
    def max_gain(self, node: "TreeNode") -> int:
        if not node:
            return 0
        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)
        path_sum = node.val + left_gain + right_gain
        self.max_sum = max(self.max_sum, path_sum)
        return node.val + max(left_gain, right_gain)