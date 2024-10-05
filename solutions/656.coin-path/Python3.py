class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        from heapq import heappop, heappush
        import sys
        
        n = len(coins)
        dp = [sys.maxsize] * n
        paths = [[] for _ in range(n)]
        
        dp[0] = coins[0]
        paths[0] = [1]
        
        for i in range(1, n):
            if coins[i] == -1:
                continue
            for j in range(max(0, i-maxJump), i):
                if dp[j] + coins[i] < dp[i]:
                    dp[i] = dp[j] + coins[i]
                    paths[i] = paths[j] + [i + 1]
                elif dp[j] + coins[i] == dp[i]:
                    new_path = paths[j] + [i + 1]
                    if new_path < paths[i]:
                        paths[i] = new_path
        
        return paths[-1] if dp[-1] != sys.maxsize else []