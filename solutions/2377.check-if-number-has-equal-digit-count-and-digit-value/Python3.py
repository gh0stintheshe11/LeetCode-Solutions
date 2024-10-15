class Solution:
    def digitCount(self, num: str) -> bool:
        count = [0] * 10
        for digit in num:
            count[int(digit)] += 1
            
        for i, digit in enumerate(num):
            if count[i] != int(digit):
                return False
        
        return True