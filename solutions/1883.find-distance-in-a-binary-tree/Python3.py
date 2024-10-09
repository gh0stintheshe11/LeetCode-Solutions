# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def findLCA(node, p, q):
            if not node or node.val == p or node.val == q:
                return node
            left = findLCA(node.left, p, q)
            right = findLCA(node.right, p, q)
            if left and right:
                return node
            return left or right
        
        def distanceFromNode(node, target, dist=0):
            if not node:
                return -1
            if node.val == target:
                return dist
            left_dist = distanceFromNode(node.left, target, dist + 1)
            if left_dist != -1:
                return left_dist
            return distanceFromNode(node.right, target, dist + 1)
        
        lca = findLCA(root, p, q)
        dist_p = distanceFromNode(lca, p)
        dist_q = distanceFromNode(lca, q)
        return dist_p + dist_q