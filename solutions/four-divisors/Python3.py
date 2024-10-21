from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_divisors(n: int) -> List[int]:
            divisors = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                if len(divisors) > 4:
                    break
            return divisors if len(divisors) == 4 else []
        
        total_sum = 0
        
        for num in nums:
            divisors = get_divisors(num)
            if divisors:
                total_sum += sum(divisors)
        
        return total_sum