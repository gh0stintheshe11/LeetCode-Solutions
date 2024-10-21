class Solution:
    def maxGcdSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ps = copy.deepcopy(nums)
        for i in range(1,n):
            ps[i] += ps[i-1]
        gcds = []
        res = 0
        for i in range(n):
            f = False
            for cgcd in gcds:
                if cgcd[0] == nums[i]:
                    f = True
                    break
            if not f:
                gcds.append([nums[i],i])
            for val, idx in gcds:
                if i-idx+1 >= k:
                    cur = (ps[i] - (0 if idx-1 < 0 else ps[idx-1])) * gcd(val, nums[i])
                    res = max(res, cur)
            rgcd = nums[i]
            newgcds = [[rgcd, i]]
            for j in range(len(gcds)-1, -1, -1):
                rgcd = gcd(rgcd, gcds[j][0])
                if rgcd == newgcds[-1][0]:
                    newgcds[-1][1] = gcds[j][1]
                else:
                    newgcds.append([rgcd, gcds[j][1]])
            gcds = list(reversed(newgcds))
        return res