# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def construct_paths(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:  # if leaf node
                    paths.append(path)
                else:
                    path += '->'
                    construct_paths(node.left, path)
                    construct_paths(node.right, path)
                    
        paths = []
        construct_paths(root, "")
        return paths