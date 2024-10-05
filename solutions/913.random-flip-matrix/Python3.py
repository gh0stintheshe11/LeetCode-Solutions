import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.flipped = {}
        self.reset()
        
    def flip(self) -> [int]:
        rand_index = random.randint(0, self.total - 1)
        pos = self.flipped.get(rand_index, rand_index)
        self.flipped[rand_index] = self.flipped.get(self.total - 1, self.total - 1)
        self.total -= 1
        return [pos // self.n, pos % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.flipped = {}