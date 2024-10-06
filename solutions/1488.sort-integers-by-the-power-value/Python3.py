class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            steps = 0
            while x != 1:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1
                steps += 1
            return steps
        
        power_values = [(i, power(i)) for i in range(lo, hi + 1)]
        power_values.sort(key=lambda x: (x[1], x[0]))
        
        return power_values[k - 1][0]