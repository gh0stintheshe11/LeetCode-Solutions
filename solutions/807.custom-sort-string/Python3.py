class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = {char: i for i, char in enumerate(order)}
        return ''.join(sorted(s, key=lambda char: order_map.get(char, len(order))))