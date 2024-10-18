class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        pnt = 0
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        ran = min(n1, n2, n3)        
        while pnt < ran and s1[pnt] == s2[pnt] == s3[pnt]:
            pnt += 1        
        if pnt == 0:
            return -1
        else:
            return (n1 + n2 + n3) - 3 * pnt