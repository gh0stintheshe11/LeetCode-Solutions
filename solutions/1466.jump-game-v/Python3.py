class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n
        
        def dfs(i):
            if dp[i] != 0:
                return dp[i]
            max_jump = 1
            for direction in [-1, 1]:
                for step in range(1, d + 1):
                    ni = i + direction * step
                    if 0 <= ni < n and arr[ni] < arr[i]:
                        max_jump = max(max_jump, 1 + dfs(ni))
                    else:
                        break
            dp[i] = max_jump
            return max_jump
        
        max_jumps = 0
        for i in range(n):
            max_jumps = max(max_jumps, dfs(i))
        
        return max_jumps