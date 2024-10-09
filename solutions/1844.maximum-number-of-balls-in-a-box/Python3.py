class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        from collections import defaultdict

        def sum_of_digits(number: int) -> int:
            s = 0
            while number > 0:
                s += number % 10
                number //= 10
            return s

        box_count = defaultdict(int)

        for ball_number in range(lowLimit, highLimit + 1):
            box_number = sum_of_digits(ball_number)
            box_count[box_number] += 1

        return max(box_count.values())