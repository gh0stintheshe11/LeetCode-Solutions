class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_index = -k - 1
        for i, num in enumerate(nums):
            if num == 1:
                if i - prev_index <= k:
                    return False
                prev_index = i
        return True