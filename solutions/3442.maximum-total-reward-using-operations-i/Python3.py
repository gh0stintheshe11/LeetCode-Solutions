class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        
        n = len(rewardValues)
        ret = 0
        seen = set()
        @cache
        
        def dfs(sum):
            nonlocal n, ret, seen
            ret = max(ret, sum)
            for i in range(n):
                if i in seen:
                    continue
                if rewardValues[i] > sum:
                    seen.add(i)
                    dfs(sum + rewardValues[i])
                    seen.remove(i)
        dfs(0)
        return ret