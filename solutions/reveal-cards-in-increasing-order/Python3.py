from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        index = deque(range(n))
        result = [0] * n
        
        for card in sorted(deck):
            result[index.popleft()] = card
            if index:
                index.append(index.popleft())
        
        return result