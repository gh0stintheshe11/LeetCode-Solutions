# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        """
            0, 1 -> False, True
            2 -> OR
            3 -> AND
            4 -> XOR
            5 -> NOT
        """
        def dfs(node):
            """
                returns (min flips for this node to True, min flips for this node to be False)
            """
            if node.val in [0,1]:
                is_true = node.val == 1
                return (0 if is_true else 1, 0 if not is_true else 1)
            
            if node.val == 5:
                if node.left:
                    res = dfs(node.left)
                    return (res[1], res[0])
                else:
                    res = dfs(node.right)
                    return (res[1], res[0])
            
            l = dfs(node.left)
            r = dfs(node.right)

            if node.val == 2:
                to_make_true = min(l[0], r[0])
                to_make_false = l[1] + r[1]

                return (to_make_true, to_make_false)
            
            if node.val == 3:
                to_make_true = l[0] + r[0]
                to_make_false = min(l[1], r[1])
                return (to_make_true, to_make_false)
            
            if node.val == 4:
                left_true_and_right_false = l[0] + r[1]
                right_true_and_left_false = l[1] + r[0]

                left_true_and_right_true = l[0] + r[0]
                left_false_and_right_false = l[1] + r[1]

                return (
                    min(left_true_and_right_false, right_true_and_left_false),
                    min(left_true_and_right_true, left_false_and_right_false),
                )

        res = dfs(root)
        if result:
            return res[0]
        
        return res[1]