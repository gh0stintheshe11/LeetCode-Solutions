import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.array = nums[:]

    def reset(self) -> List[int]:
        self.array = self.original[:]
        return self.array

    def shuffle(self) -> List[int]:
        shuffled = self.array[:]
        random.shuffle(shuffled)
        return shuffled