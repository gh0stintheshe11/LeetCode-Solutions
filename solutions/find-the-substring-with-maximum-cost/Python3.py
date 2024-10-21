class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        value_map = {c: v for c, v in zip(chars, vals)}

        def get_value(c):
            if c in value_map:
                return value_map[c]
            else:
                return ord(c) - ord('a') + 1

        max_cost = 0
        current_cost = 0

        for char in s:
            current_cost += get_value(char)
            if current_cost < 0:
                current_cost = 0
            max_cost = max(max_cost, current_cost)

        return max_cost