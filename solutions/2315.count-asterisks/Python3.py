class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        is_between_bars = False
        for char in s:
            if char == '|':
                is_between_bars = not is_between_bars
            elif char == '*' and not is_between_bars:
                count += 1
        return count