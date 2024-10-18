class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_amount = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                shift_amount[start] += 1
                shift_amount[end + 1] -= 1
            else:
                shift_amount[start] -= 1
                shift_amount[end + 1] += 1

        current_shift = 0
        result = []

        for i in range(n):
            current_shift += shift_amount[i]
            new_char = chr(((ord(s[i]) - ord('a') + current_shift) % 26) + ord('a'))
            result.append(new_char)

        return ''.join(result)