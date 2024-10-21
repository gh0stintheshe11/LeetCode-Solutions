# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter

class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        def countLeaves(node):
            if not node:
                return Counter()
            if not node.left and not node.right:
                return Counter({node.val: 1})
            return countLeaves(node.left) + countLeaves(node.right)
        
        return countLeaves(root1) == countLeaves(root2)