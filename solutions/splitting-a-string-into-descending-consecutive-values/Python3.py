class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(index, prev_value):
            if index == len(s):
                return True

            current_number = 0
            for i in range(index, len(s)):
                current_number = current_number * 10 + int(s[i])
                if prev_value - 1 == current_number:
                    if backtrack(i + 1, current_number):
                        return True
                elif current_number >= prev_value:
                    break
                
            return False

        for i in range(1, len(s)):
            first_number = int(s[:i])
            if backtrack(i, first_number):
                return True

        return False