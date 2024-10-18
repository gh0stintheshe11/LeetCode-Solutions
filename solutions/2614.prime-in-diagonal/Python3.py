from typing import List
import math

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n: int) -> bool:
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        max_prime = 0
        length = len(nums)
        
        # Check primary diagonal
        for i in range(length):
            if is_prime(nums[i][i]):
                max_prime = max(max_prime, nums[i][i])
        
        # Check secondary diagonal
        for i in range(length):
            if is_prime(nums[i][length - i - 1]):
                max_prime = max(max_prime, nums[i][length - i - 1])
        
        return max_prime