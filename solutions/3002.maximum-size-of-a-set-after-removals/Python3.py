class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        return min(len(set(nums1 + nums2)), min(len(set(nums1)), len(nums1) // 2) + min(len(set(nums2)), len(nums2) // 2))