class Solution:
    def countArrangement(self, n: int) -> int:
        def count(i, X):
            if i == 1: 
                return 1
            return sum(count(i - 1, X - {x}) for x in X if x % i == 0 or i % x == 0)
        
        return count(n, set(range(1, n + 1)))