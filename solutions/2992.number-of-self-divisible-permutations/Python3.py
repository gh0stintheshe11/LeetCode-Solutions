class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        def backtrack(pos, used_mask):
            if pos > n:
                return 1
            count = 0
            for num in range(1, n + 1):
                if not used_mask & (1 << (num - 1)) and math.gcd(num, pos) == 1:
                    count += backtrack(pos + 1, used_mask | (1 << (num - 1)))
            return count

        import math
        return backtrack(1, 0)