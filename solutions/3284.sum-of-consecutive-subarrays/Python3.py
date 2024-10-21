class Solution:
    def getSum(self, nums: List[int]) -> int:
        def cons_sum(le, ri):
            l = 0
            r = ri - le + 2
            res = 0
            for _ in range(ri - le + 1):
                l += 1
                r -= 1
                res = (res + nums[le + l - 1] * l * r) % MOD
            return res

        n = len(nums)
        MOD = 1_000_000_007
        prev = 0
        nums.append(-999)

        le = ri = ans = 0
        for i in range(n):
            dif = nums[i + 1] - nums[i]
            if (not prev and dif in (1, -1)) or (prev and prev == dif):
                if not prev:
                    prev = dif
                ri += 1
            else:
                ans = (ans + cons_sum(le, ri)) % MOD
                if dif in (1, -1):
                    prev = dif
                    le = i
                    ri = i + 1
                    ans = (ans - nums[i]) % MOD
                else:
                    le = ri = i + 1
                    prev = 0
        return ans