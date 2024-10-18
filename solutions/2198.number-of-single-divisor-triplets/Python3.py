class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        ans, items, n = 0, list(c.items()), len(c)
        for i1, (k1, v1) in enumerate(items):                       # 3 unique keys
            for i2, (k2, v2) in enumerate(items[i1+1:], i1+1):
                for i3, (k3, v3) in enumerate(items[i2+1:], i2+1):
                    cur = k1 + k2 + k3
                    a1 = 1 - (cur % k1 == 0)
                    a2 = 1 - (cur % k2 == 0)
                    a3 = 1 - (cur % k3 == 0)
                    if a1 + a2 + a3 == 2:
                        ans += v1 * v2 * v3 * 6
        for i1, (k1, v1) in enumerate(items):                       # 2 unique keys, one key will be used twice
            if v1 == 1: continue
            for i2, (k2, v2) in enumerate(items):
                if i1 == i2: continue
                cur = 2 * k1 + k2
                if cur % k1 and cur % k2 == 0:
                    ans += v1 * (v1-1) * v2 * 3
        return ans