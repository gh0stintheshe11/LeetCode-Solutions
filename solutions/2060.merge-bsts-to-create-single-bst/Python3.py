# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        from collections import defaultdict, Counter
        
        # Store trees by root value and leaf frequencies
        nodes_by_val = {tree.val: tree for tree in trees}
        leaf_count = Counter()
        
        # Populate leaf value count
        for tree in trees:
            if tree.left:
                leaf_count[tree.left.val] += 1
            if tree.right:
                leaf_count[tree.right.val] += 1
        
        # All possible children values
        possible_children = set(leaf_count.keys())
        
        # Identify the main root (which is not a leaf in any other tree)
        trees_root_values = set(nodes_by_val.keys())
        candidate_roots = trees_root_values - possible_children
        
        if len(candidate_roots) != 1:
            return None
        
        main_root_val = candidate_roots.pop()
        main_root = nodes_by_val[main_root_val]

        def can_form_bst(node, low, high, available_nodes):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            if node.left and node.left.val in available_nodes:
                node.left = available_nodes.pop(node.left.val)
            if node.right and node.right.val in available_nodes:
                node.right = available_nodes.pop(node.right.val)
            return can_form_bst(node.left, low, node.val, available_nodes) and can_form_bst(node.right, node.val, high, available_nodes)

        available_nodes = nodes_by_val.copy()
        available_nodes.pop(main_root.val)

        if not can_form_bst(main_root, float("-inf"), float("inf"), available_nodes):
            return None
        
        return main_root if not available_nodes else None