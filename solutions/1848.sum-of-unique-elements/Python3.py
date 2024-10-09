class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        return sum(num for num, freq in count.items() if freq == 1)