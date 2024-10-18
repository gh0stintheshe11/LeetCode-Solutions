class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for n in range(1, 11):
            if n * k % 10 == num % 10 and n * k <= num:
                return n
        return -1