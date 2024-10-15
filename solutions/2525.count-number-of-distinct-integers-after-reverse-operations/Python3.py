class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct_numbers = set(nums)
        for num in nums:
            reversed_num = int(str(num)[::-1])
            distinct_numbers.add(reversed_num)
        return len(distinct_numbers)