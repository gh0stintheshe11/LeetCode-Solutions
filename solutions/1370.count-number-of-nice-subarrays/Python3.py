class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            count = 0
            left = 0
            res = 0
            for right, value in enumerate(nums):
                if value % 2 == 1:
                    k -= 1
                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1
                    left += 1
                res += right - left + 1
            return res
        
        return atMostK(k) - atMostK(k - 1)