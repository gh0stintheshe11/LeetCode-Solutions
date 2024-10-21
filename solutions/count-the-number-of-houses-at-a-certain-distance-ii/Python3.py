class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x
        if x == y or x + 1 == y:
            return [2 * (n - dist) for dist in range(1, n + 1)]

        lhs_linear_size = x
        rhs_linear_size = n - y + 1
        ring_size = y - x + 1
        fan_size = (ring_size - 1) // 2

        num_pairs = [0] * (n + 1)

        for dist in range(1, fan_size + 1):
            num_pairs[dist] += 2 * ring_size
        if fan_size * 2 + 1 < ring_size:
            num_pairs[fan_size + 1] += ring_size
        if ring_size == n:
            return num_pairs[1:]
            
        num_nodes = min(lhs_linear_size + rhs_linear_size, n)
        for dist in range(1, num_nodes):
            num_pairs[dist] += 2 * (num_nodes - dist)
        num_pairs[1] += 2
        for num_nodes in [lhs_linear_size, rhs_linear_size]:
            for dist in range(1, num_nodes + 1):
                num_pairs[dist] -= 2
            
        if fan_size * 2 + 1 < ring_size:
            for num_nodes in [lhs_linear_size, rhs_linear_size]:
                for dist in range(1, num_nodes):
                    num_pairs[dist + fan_size + 1] += 2

        if fan_size > 0:
            for num_nodes in [lhs_linear_size, rhs_linear_size]:
                if num_nodes < 2:
                    continue
                min_dist = 1 + 1
                max_dist = (num_nodes - 1) + fan_size
                num_fans = 2
                for dist in range(min_dist, max_dist + 1):
                    mult = min(1 + min(dist - min_dist, max_dist - dist), fan_size, num_nodes - 1)
                    num_pairs[dist] += mult * num_fans * 2               

        return num_pairs[1:]