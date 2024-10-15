class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])
        
        MOD = 10**9 + 7
        count = Counter()
        nice_pairs = 0
        
        for num in nums:
            diff = num - rev(num)
            nice_pairs = (nice_pairs + count[diff]) % MOD
            count[diff] += 1
        
        return nice_pairs