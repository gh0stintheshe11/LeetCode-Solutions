class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        k = 0
        while (k * (k + 1)) // 2 <= n:
            k += 1
        return k - 1