class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        freq = {}
        
        for num in nums:
            count += freq.get(num - k, 0) + freq.get(num + k, 0)
            freq[num] = freq.get(num, 0) + 1
        
        return count