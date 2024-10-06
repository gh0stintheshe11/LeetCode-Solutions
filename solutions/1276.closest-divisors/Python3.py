import math
from typing import List

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def find_closest(n: int) -> List[int]:
            # Iterate downward from sqrt(n) to find the closest pair of divisors
            for i in range(int(math.sqrt(n)), 0, -1):
                if n % i == 0:
                    return [i, n // i]
            return []
        
        num1, num2 = num + 1, num + 2
        divisors1 = find_closest(num1)
        divisors2 = find_closest(num2)
        
        # Compare which pair is closer
        if abs(divisors1[0] - divisors1[1]) <= abs(divisors2[0] - divisors2[1]):
            return divisors1
        else:
            return divisors2