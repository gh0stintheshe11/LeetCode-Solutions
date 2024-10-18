from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_seen = {}
        min_length = float('inf')
        
        for i, card in enumerate(cards):
            if card in last_seen:
                min_length = min(min_length, i - last_seen[card] + 1)
            last_seen[card] = i
        
        return min_length if min_length != float('inf') else -1