class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [(root, root.val)]  # [node, siblings_sum]
        level_sum = root.val  # sum of nodes at a level
        
        # BFS
        while queue:
            curr = 0
            level_q = []
            for node, sib in queue:
                node.val = level_sum - sib  # replace node value with sum of siblings
                next_sib = 0
                if node.left:
                    next_sib += node.left.val
                if node.right:
                    next_sib += node.right.val
                curr += next_sib
                if node.left:
                    level_q.append((node.left, next_sib))
                if node.right:
                    level_q.append((node.right, next_sib))
            queue = level_q
            level_sum = curr  # update sum of nodes at current level
        return root