class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for digit in "9876543210":
            triplet = digit * 3
            if triplet in num:
                return triplet
        return ""