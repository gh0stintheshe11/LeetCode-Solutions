# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.deque = collections.deque()
        
        # Level order traversal to populate deque with leaf nodes
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        node = self.deque[0]
        
        if not node.left:
            node.left = new_node
        else:
            node.right = new_node
            self.deque.popleft()

        self.deque.append(new_node)
        
        return node.val

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()