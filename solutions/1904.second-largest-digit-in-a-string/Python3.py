class Solution:
    def secondHighest(self, s: str) -> int:
        highest, second_highest = -1, -1
        for char in s:
            if char.isdigit():
                digit = int(char)
                if digit > highest:
                    second_highest, highest = highest, digit
                elif digit > second_highest and digit != highest:
                    second_highest = digit
        return second_highest