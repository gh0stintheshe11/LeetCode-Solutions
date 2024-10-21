class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        flip_count = [0] * (n + 1)

        for query in queries:
            flip_count[query] += 1

        result = 0

        for v in range(1, n + 1):
            c = 0
            node = v
            while node > 0:
                c += flip_count[node]
                node //= 2
            if c % 2 == 1:
                result += 1

        return result