class Solution:
    def sortedArrayToBST(self, nums):
        def convert(nums, start, end):
            if end < start:
                return None

            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = convert(nums, start, mid - 1)
            node.right = convert(nums, mid + 1, end)
            return node
        return convert(nums, 0, len(nums) - 1)