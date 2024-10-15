# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        child_set = set()
        
        # Create nodes and link them according to descriptions
        for parent, child, isLeft in descriptions:
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
            if child not in node_map:
                node_map[child] = TreeNode(child)
            
            if isLeft:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]
            
            child_set.add(child)
        
        # The root is the node that is never a child
        for parent, _, _ in descriptions:
            if parent not in child_set:
                return node_map[parent]
        
        return None