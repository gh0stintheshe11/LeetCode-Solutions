class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict

        def digit_sum(x):
            return sum(int(d) for d in str(x))

        groups = defaultdict(int)

        for i in range(1, n + 1):
            s = digit_sum(i)
            groups[s] += 1

        max_size = max(groups.values())
        return sum(1 for size in groups.values() if size == max_size)