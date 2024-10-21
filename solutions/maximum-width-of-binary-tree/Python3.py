
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q, width = deque([(root, 0)]), 0
        while q:
            width = max(width, q[-1][1] - q[0][1])
            for _ in range(len(q)):
                node, k = q.popleft()
                if node.left:
                    q.append((node.left, k * 2 - 1))
                if node.right:
                    q.append((node.right, k * 2))
        return width + 1

