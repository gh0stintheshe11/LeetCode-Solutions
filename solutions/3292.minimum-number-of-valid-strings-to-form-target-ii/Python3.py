class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        left = 0
        right = 1
        n = len(target)
        dp = [0] * (n + 1)

        while right <= n:
            if left == right:
                return -1
            if self.isValidPrefix(words, target[left:right]):    
                dp[right] = dp[left] + 1
                right += 1
            else:
                left += 1
        return dp[-1]

    def isValidPrefix(self, words, prefix):
        for word in words:
            if word.startswith(prefix):
                return True
        return False