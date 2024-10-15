class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10**9 + 7
        # Total possible movements for the monkeys is 2^n (each monkey has 2 choices)
        total_moves = pow(2, n, MOD)
        # Subtract the two non-collision scenarios (all clockwise or all counterclockwise)
        collision_ways = (total_moves - 2) % MOD
        return collision_ways