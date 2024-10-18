class Solution:
    def lastVisitedIntegers(self, nums: list[int]) -> list[int]:
        seen = []
        ans = []
        k = 0
        for num in nums:
            if num != -1:
                seen.insert(0, num)
                k = 0
            else:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)
        return ans