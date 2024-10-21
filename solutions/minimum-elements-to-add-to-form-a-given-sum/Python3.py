class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        current_sum = sum(nums)
        difference = abs(goal - current_sum)
        return (difference + limit - 1) // limit