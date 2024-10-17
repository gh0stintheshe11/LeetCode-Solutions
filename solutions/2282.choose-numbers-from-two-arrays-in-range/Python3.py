class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0 
        mod = 1_000_000_007 
        freq = defaultdict(int)
        for x, y in zip(nums1, nums2): 
            ff = defaultdict(int)
            ff[x] += 1
            ff[-y] += 1
            for k, v in freq.items(): 
                ff[k+x] += v
                ff[k-y] += v
            freq = ff
            ans = (ans + freq[0]) % mod 
        return ans