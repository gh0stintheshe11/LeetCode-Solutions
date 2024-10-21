class Solution:
    def minimumBoxes(self, n: int) -> int:
        def sum_of_integers(x):
            return x * (x + 1) // 2

        # Find maximum k such that 1 + 2 + ... + k <= n
        total, k = 0, 0
        while total + (k + 1) * (k + 2) // 2 <= n:
            k += 1
            total += k * (k + 1) // 2
        
        # Find additional boxes needed on top of the k layers
        remaining = n - total
        h = 0
        while h * (h + 1) // 2 < remaining:
            h += 1
        
        return k * (k + 1) // 2 + h