class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        current = '0'
        for bit in target:
            if bit != current:
                flips += 1
                current = bit
        return flips