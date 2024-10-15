class Solution:
    def findGCD(self, nums: List[int]) -> int:
        from math import gcd
        return gcd(min(nums), max(nums))