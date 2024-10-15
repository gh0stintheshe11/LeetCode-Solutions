# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
from typing import Optional

class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        graph = defaultdict(list)
        leaves = set()

        def build_graph(node: Optional[TreeNode]):
            if node:
                if node.left is None and node.right is None:
                    leaves.add(node.val)
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    build_graph(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    build_graph(node.right)

        build_graph(root)
        
        queue = deque([k])
        visited = set([k])
        
        while queue:
            current = queue.popleft()
            if current in leaves:
                return current
                
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return -1