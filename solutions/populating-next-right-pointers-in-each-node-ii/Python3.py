class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        q = [root]
        while q:
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                if i < size - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root