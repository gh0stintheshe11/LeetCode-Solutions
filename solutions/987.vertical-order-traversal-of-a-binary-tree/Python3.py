# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import List, Optional

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = collections.defaultdict(list)

        def dfs(node, row, col):
            if node:
                nodes[col].append((row, node.val))
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        sorted_columns = sorted(nodes.keys())
        result = []
        for col in sorted_columns:
            column_nodes = sorted(nodes[col], key=lambda x: (x[0], x[1]))
            column_vals = [val for row, val in column_nodes]
            result.append(column_vals)

        return result