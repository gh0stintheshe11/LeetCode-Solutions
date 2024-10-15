class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7

        # Calculate distance to move
        distance = abs(endPos - startPos)

        # If the distance is greater than k or if (k - distance) is odd, it's impossible
        if distance > k or (k - distance) % 2 != 0:
            return 0

        # Number of steps to the right
        right_steps = (k + distance) // 2
        # Number of steps to the left
        left_steps = (k - distance) // 2

        # Calculate combination "k choose right_steps"
        def combination(n, r):
            if r > n:
                return 0
            c = 1
            for i in range(r):
                c = c * (n - i) // (i + 1)
            return c

        return combination(k, right_steps) % MOD