class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        sorted_s2 = sorted(s2)
        
        def can_break(x, y):
            return all(x[i] >= y[i] for i in range(len(x)))
        
        return can_break(sorted_s1, sorted_s2) or can_break(sorted_s2, sorted_s1)