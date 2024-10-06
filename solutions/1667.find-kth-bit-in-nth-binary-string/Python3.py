class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s: str) -> str:
            return ''.join('1' if c == '0' else '0' for c in s)

        def construct_string(n: int) -> str:
            if n == 1:
                return "0"
            prev = construct_string(n - 1)
            return prev + "1" + invert(prev)[::-1]

        return construct_string(n)[k - 1]