class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1
        count = 9
        start = 1

        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10

        start += (n - 1) // digit_length
        s = str(start)
        return int(s[(n - 1) % digit_length])