class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        divisible_count = n // m
        last_divisible = divisible_count * m
        divisible_sum = divisible_count * (m + last_divisible) // 2
        non_divisible_sum = total_sum - divisible_sum
        return non_divisible_sum - divisible_sum