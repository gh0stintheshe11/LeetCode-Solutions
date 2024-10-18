class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums_set = set(nums)
        for i in range(1 << n):
            candidate = format(i, '0' + str(n) + 'b')
            if candidate not in nums_set:
                return candidate