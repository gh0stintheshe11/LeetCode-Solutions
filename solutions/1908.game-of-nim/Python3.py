class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        xor_sum = 0
        for pile in piles:
            xor_sum ^= pile
        return xor_sum != 0