class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        max_happiness = 0
        for i in range(k):
            max_happiness += max(0, happiness[i] - i)
        return max_happiness