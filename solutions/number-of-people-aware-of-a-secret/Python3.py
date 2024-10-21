from collections import Counter

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        if n <= delay:
            return 1
        
        current = 0

        delays = Counter()
        delays[delay + 1] = 1
        forgets = Counter()
        forgets[forget + 1] = 1

        for day in range(delay + 1, n + 1):
            current = (
                current
                + delays.pop(day, 0)
                - forgets.pop(day, 0)
            )
            delays[day + delay] += current
            forgets[day + forget] += current

        return (
            current + sum(delays.values())
        ) % 1_000_000_007