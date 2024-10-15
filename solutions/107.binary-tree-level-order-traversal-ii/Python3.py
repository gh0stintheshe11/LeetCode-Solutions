from collections import deque
class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        result = deque()
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.appendleft(level)
        return list(result)