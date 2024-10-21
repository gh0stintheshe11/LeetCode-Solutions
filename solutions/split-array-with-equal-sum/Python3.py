class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if n < 7:
            return False
        
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        
        for j in range(3, n - 3):
            seen_sums = set()
            for i in range(1, j - 1):
                if prefix[i - 1] == prefix[j - 1] - prefix[i]:
                    seen_sums.add(prefix[i - 1])
            for k in range(j + 2, n - 1):
                if (prefix[n - 1] - prefix[k] == prefix[k - 1] - prefix[j] and 
                    prefix[n - 1] - prefix[k] in seen_sums):
                    return True
        return False