class Solution:
    def recoverTree(self, root):
        def findTwoSwapped(root: TreeNode):
            nonlocal x, y, pred
            if root is None:
                return
            
            findTwoSwapped(root.left)
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred 
                else:
                    return
            pred = root
            findTwoSwapped(root.right)

        x = y = pred = None
        findTwoSwapped(root)
        x.val, y.val = y.val, x.val