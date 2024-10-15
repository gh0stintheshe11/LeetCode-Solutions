from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        power_of_twos = [1 << i for i in range(22)]
        count = defaultdict(int)
        result = 0
        
        for value in deliciousness:
            for target in power_of_twos:
                if target - value in count:
                    result += count[target - value]
                    result %= MOD
            count[value] += 1
        
        return result