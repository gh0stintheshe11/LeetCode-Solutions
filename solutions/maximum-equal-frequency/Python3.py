class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        count = defaultdict(int)
        freq = defaultdict(int)
        max_length = 0
        max_freq = 0
        
        for i, num in enumerate(nums):
            if count[num] > 0:
                freq[count[num]] -= 1
                if freq[count[num]] == 0:
                    del freq[count[num]]
            
            count[num] += 1
            max_freq = max(max_freq, count[num])
            freq[count[num]] += 1
            
            # Check if possible to remove 1 element to make the remaining all appear with same frequency
            if (
                max_freq == 1 or
                (max_freq * freq[max_freq] + 1 == i + 1) or
                ((max_freq - 1) * (freq[max_freq - 1] + 1) + 1 == i + 1)
            ):
                max_length = i + 1
        
        return max_length