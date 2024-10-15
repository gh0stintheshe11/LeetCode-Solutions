from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)

        # Calculate prefix sum
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = (prefix_sum[i] + strength[i]) % MOD

        # Calculate prefix of prefix sum
        prefix_sum2 = [0] * (n + 2)
        for i in range(n + 1):
            prefix_sum2[i + 1] = (prefix_sum2[i] + prefix_sum[i]) % MOD

        # Finding previous less and next less elements
        left = [-1] * n
        right = [n] * n

        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # Calculate the total strength
        total_strength = 0
        for i in range(n):
            l = left[i]
            r = right[i]
            total_right = (prefix_sum2[r + 1] - prefix_sum2[i + 1]) * (i - l)
            total_left = (prefix_sum2[i + 1] - prefix_sum2[l + 1]) * (r - i)

            contrib = (total_right - total_left) % MOD
            total_strength = (total_strength + strength[i] * contrib) % MOD

        return total_strength