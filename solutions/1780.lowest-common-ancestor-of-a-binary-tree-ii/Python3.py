# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findLCAAndCheckExistence(node):
            if not node:
                return None, False, False
            
            leftLCA, leftFoundP, leftFoundQ = findLCAAndCheckExistence(node.left)
            rightLCA, rightFoundP, rightFoundQ = findLCAAndCheckExistence(node.right)
            
            foundP = (node == p) or leftFoundP or rightFoundP
            foundQ = (node == q) or leftFoundQ or rightFoundQ

            if node == p or node == q:
                return node, foundP, foundQ

            if leftLCA and rightLCA:
                return node, foundP, foundQ
            
            if leftLCA:
                return leftLCA, foundP, foundQ
            
            if rightLCA:
                return rightLCA, foundP, foundQ
            
            return None, foundP, foundQ

        lca, foundP, foundQ = findLCAAndCheckExistence(root)
        if foundP and foundQ:
            return lca
        return None