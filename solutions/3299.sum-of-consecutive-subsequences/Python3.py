class Solution:
    def getSum(self, nums: List[int]) -> int:
        res = 0
        freq = {}
        for a in nums:
            if a not in freq:
                freq[a] = [1, a]
            else:
                freq[a][0] += 1
                freq[a][1] += a % (10**9+7)
            if a-1 in freq:
                freq[a][0] += freq[a-1][0]
                freq[a][1] += (a*freq[a-1][0] + freq[a-1][1]) % (10**9+7)
            freq[a][1] = freq[a][1] % (10**9+7)
        res += sum(a[1] for a in freq.values()) % (10**9+7)
        freq = {}
        for a in nums:
            if a not in freq:
                freq[a] = [1, a]
            else:
                freq[a][0] += 1
                freq[a][1] += a % (10**9+7)
            if a+1 in freq:
                freq[a][0] += freq[a+1][0]
                freq[a][1] += (a*freq[a+1][0] + freq[a+1][1]) % (10**9+7)
            freq[a][1] = freq[a][1] % (10**9+7)
        res += sum(a[1] for a in freq.values()) % (10**9+7)
        return (res - sum(nums)) % (10**9+7)