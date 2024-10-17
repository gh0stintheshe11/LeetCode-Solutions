class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max_num1 = max(nums1)
        res = 0
        nums1_ctr = Counter(nums1)
        nums2_ctr = Counter(nums2)
        for num2 in nums2_ctr:
            mul = 1
            while num2 * k * mul <= max_num1:
                res += nums2_ctr[num2] * nums1_ctr[num2 * k * mul]
                mul += 1
        return res