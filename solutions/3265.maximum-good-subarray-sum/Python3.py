class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = collections.defaultdict(int)
        ssum = 0
        maxval = -inf

        for num in nums:
            if num in seen:
                subarraysum = ssum + num - seen[num]
                maxval = max(maxval, subarraysum)
            if num+k in seen:
                seen[num+k] = min(seen[num+k], ssum)
            else:
                seen[num+k] = ssum
            if num-k in seen:
                seen[num-k] = min(seen[num-k], ssum)
            else:
                seen[num-k] = ssum
            ssum += num
        
        return maxval if maxval != -inf else 0