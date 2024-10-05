# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if not node:
                return ['null']
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        
        return '[' + ','.join(preorder(root)) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data[1:-1].split(',')
        
        def build_tree(data_iter):
            val = next(data_iter)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = build_tree(data_iter)
            node.right = build_tree(data_iter)
            return node
        
        return build_tree(iter(data_list))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))