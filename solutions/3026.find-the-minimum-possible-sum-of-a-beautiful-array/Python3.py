class Solution:
    def getSumOfAP(self, numTerms: int, firstTerm: int, lastTerm: int) -> int:
        if numTerms % 2 == 0:
            return (numTerms // 2) * (firstTerm + lastTerm)
        else:
            return ((firstTerm + lastTerm) // 2) * numTerms

    def minimumPossibleSum(self, n: int, target: int) -> int:
        firstTerm, lastTerm = target // 2, target
        if firstTerm > n:
            return self.getSumOfAP(n, 1, n) % 1000000007
        return (self.getSumOfAP(firstTerm, 1, firstTerm) + self.getSumOfAP((n - firstTerm), lastTerm, (lastTerm + n - firstTerm - 1))) % 1000000007