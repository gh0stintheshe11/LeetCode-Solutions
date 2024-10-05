class Solution(object):
    def romanToInt(self, s):
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        i = len(s) - 1
        num = 0
        while i >= 0:
            if i - 1 >= 0 and s[i-1:i+1] in map:
                num += map[s[i-1:i+1]]
                i -= 2
            else:
                num += map[s[i]]
                i -= 1
        return num