class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_str = str(n)
        parts = []
        while n_str:
            parts.append(n_str[-3:])
            n_str = n_str[:-3]
        return '.'.join(parts[::-1])