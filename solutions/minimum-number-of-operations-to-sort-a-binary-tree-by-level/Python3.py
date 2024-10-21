# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        def min_swaps_to_sort(nums):
            n = len(nums)
            arrpos = [(num, i) for i, num in enumerate(nums)]
            arrpos.sort()
            vis = {i: False for i in range(n)}
            ans = 0
            for i in range(n):
                if vis[i] or arrpos[i][1] == i:
                    continue
                cycle_size = 0
                j = i
                while not vis[j]:
                    vis[j] = True
                    j = arrpos[j][1]
                    cycle_size += 1
                if cycle_size > 0:
                    ans += (cycle_size - 1)
            return ans

        level_order = []
        queue = deque([root])
        while queue:
            level_length = len(queue)
            current_level = []
            for _ in range(level_length):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_order.append(current_level)

        min_ops = 0
        for level in level_order:
            min_ops += min_swaps_to_sort(level)

        return min_ops