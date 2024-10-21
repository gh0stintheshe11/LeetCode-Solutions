class Solution:
    def findNumber(self) -> int:
        result = 0
        for i in range(30):
            if commonSetBits(1 << i) > 0:
                result |= (1 << i)
        return result