import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        return random.choice([i for i, num in enumerate(self.nums) if num == target])