class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        common_digits = set(nums1).intersection(nums2)
        if common_digits:
            return min(common_digits)
        
        smallest1 = min(nums1)
        smallest2 = min(nums2)
        return min(smallest1 * 10 + smallest2, smallest2 * 10 + smallest1)