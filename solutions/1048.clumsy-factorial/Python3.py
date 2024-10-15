class Solution:
    def clumsy(self, n: int) -> int:
        # Handling for base cases
        if n == 1: return 1
        if n == 2: return 2 * 1
        if n == 3: return 3 * 2 // 1
        if n == 4: return 4 * 3 // 2 + 1

        # For n > 4, compute in blocks of 4 and manage remainder
        if n % 4 == 0: return n + 1
        elif n % 4 == 1: return n + 2
        elif n % 4 == 2: return n + 2
        else: return n - 1