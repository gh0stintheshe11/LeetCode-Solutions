from typing import List
from itertools import accumulate
import bisect

class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        m_pairs = list(zip(monsters, coins))
        m_pairs.sort()
        
        sorted_monsters, sorted_coins = zip(*m_pairs)
        
        coin_prefix_sum = list(accumulate(sorted_coins))
        
        result = []
        for hero in heroes:
            pos = bisect.bisect_right(sorted_monsters, hero)
            if pos > 0:
                result.append(coin_prefix_sum[pos - 1])
            else:
                result.append(0)
        
        return result