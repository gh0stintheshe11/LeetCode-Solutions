class Solution:
    def minimumOperations(self, num: str) -> int:
        @cache
        def dp(index, curNum):
            if index == len(num):
                return float('inf') if curNum % 25 else 0 
            return min(dp(index + 1, (curNum * 10 + int(num[index])) % 25), dp(index + 1, curNum) + 1)
        return dp(0, 0)