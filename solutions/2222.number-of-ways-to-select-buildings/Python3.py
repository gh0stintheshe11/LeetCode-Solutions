class Solution:
    def numberOfWays(self, s: str) -> int:
        count0 = 0
        count1 = 0
        count01 = 0
        count10 = 0
        count010 = 0
        count101 = 0
        
        for char in s:
            if char == '0':
                count010 += count10
                count01 += count1
                count0 += 1
            else:  # char == '1'
                count101 += count01
                count10 += count0
                count1 += 1
        
        return count010 + count101