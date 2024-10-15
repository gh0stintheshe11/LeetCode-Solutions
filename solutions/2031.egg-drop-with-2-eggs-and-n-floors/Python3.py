class Solution:
    def twoEggDrop(self, n: int) -> int:
        # The problem reduces to finding the minimum number k such that
        # k + (k-1) + (k-2) + ... + 1 >= n, which is the smallest triangular number larger than or equal to n.
        k = 0
        while k * (k + 1) // 2 < n:
            k += 1
        return k