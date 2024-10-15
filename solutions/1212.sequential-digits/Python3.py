class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequential_digits = []
        s = "123456789"
        for length in range(2, 10): # lengths from 2 to 9
            for start in range(10 - length): # start index for substring
                num = int(s[start:start + length])
                if low <= num <= high:
                    sequential_digits.append(num)
        return sorted(sequential_digits)