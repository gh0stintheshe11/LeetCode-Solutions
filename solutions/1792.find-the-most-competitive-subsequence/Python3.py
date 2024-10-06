class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        to_remove = len(nums) - k
        for num in nums:
            while stack and to_remove > 0 and stack[-1] > num:
                stack.pop()
                to_remove -= 1
            stack.append(num)
        
        return stack[:k]