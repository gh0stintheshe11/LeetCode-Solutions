# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int):
        if n % 2 == 0:  # If n is even, it's not possible to form a full binary tree
            return []
        
        # Memoization to store results for subproblems
        memo = {}
        
        def generateFBT(n):
            if n in memo:
                return memo[n]
            
            if n == 1:
                return [TreeNode(0)]
            
            result = []
            for left_nodes in range(1, n, 2):
                right_nodes = n - 1 - left_nodes
                left_trees = generateFBT(left_nodes)
                right_trees = generateFBT(right_nodes)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)
            
            memo[n] = result
            return result
        
        return generateFBT(n)
