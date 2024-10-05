class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        if not root.left and not root.right and root.val == targetSum:
            return [[root.val]]
        temp = self.pathSum(root.left, targetSum-root.val) + self.pathSum(root.right, targetSum-root.val)
        return [[root.val]+i for i in temp]