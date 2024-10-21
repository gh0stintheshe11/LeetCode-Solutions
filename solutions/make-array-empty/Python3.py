from collections import defaultdict

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        ans = 0
        i += 1
        while i > 0:
            ans += self.tree[i]
            i -= (i & (-i))
        return ans

    def update(self, i, value):
        i += 1
        while i <= self.n:
            self.tree[i] += value
            i += (i & (-i))

class Solution:
    def countOperationsToEmptyArray(self, nums) -> int:
        mp = defaultdict(int)
        for id, i in enumerate(nums):
            mp[i] = id
        n = len(nums)
        bt = BIT(n)
        for i in range(n):
            bt.update(i, 1)
        last = -1
        ans = 0
        for i in sorted(nums):
            li = 0
            bt.update(mp[i], -1)
            if last == -1:
                ans += bt.sum(mp[i]) + 1
                last = mp[i]
            elif last < mp[i]:
                ans += bt.sum(mp[i]) - bt.sum(last) + 1
                last = mp[i]
            elif last > mp[i]:
                li = bt.sum(n - 1) - bt.sum(last)
                ans += bt.sum(mp[i]) + li + 1
                last = mp[i]
                
        return ans