from typing import List

class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(nums)
        B = int(n**0.5) + 1
        
        # Preprocess for y values <= B
        precomputed_sums = [[0] * n for _ in range(B)]
        
        for y in range(1, B):
            for x in range(n - 1, -1, -1):
                precomputed_sums[y][x] = nums[x]
                if x + y < n:
                    precomputed_sums[y][x] += precomputed_sums[y][x + y]
        
        answer = []
        
        for x, y in queries:
            if y < B:
                answer.append(precomputed_sums[y][x] % MOD)
            else:
                total = 0
                for j in range(x, n, y):
                    total += nums[j]
                answer.append(total % MOD)
        
        return answer