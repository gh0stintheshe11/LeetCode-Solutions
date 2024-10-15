# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def preorder(node):
            return [node.val] + preorder(node.left) + preorder(node.right) if node else []
        
        return ' '.join(map(str, preorder(root)))
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        data_list = list(map(int, data.split()))
        
        def build_bst(min_val, max_val):
            if data_list and min_val < data_list[0] < max_val:
                val = data_list.pop(0)
                node = TreeNode(val)
                node.left = build_bst(min_val, val)
                node.right = build_bst(val, max_val)
                return node
            return None
        
        return build_bst(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans