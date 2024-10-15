class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a' * n if n % 2 != 0 else 'a' * (n - 1) + 'b'