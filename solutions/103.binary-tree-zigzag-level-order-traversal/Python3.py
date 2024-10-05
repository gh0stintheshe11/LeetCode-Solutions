class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        
        queue = [(root, 0)]
        res = []
        
        while queue:
            node, level = queue.pop(0)
            if len(res) < level + 1:
                res.append([])
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return res