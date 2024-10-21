class Solution:
    def maxSpending(self, v: List[List[int]]) -> int:
        res = []
        for i in range(len(v)):
            for j in range(len(v[0])):
                res.append(v[i][j])
        ans = 0
        res.sort()
        l = 1
        for i in res:
            ans += l * i
            l += 1
        return ans