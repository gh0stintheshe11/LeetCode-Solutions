import collections
import random

class RandomizedCollection:

    def __init__(self):
        self.idx_map = collections.defaultdict(set)
        self.values = []

    def insert(self, val: int) -> bool:
        self.values.append(val)
        self.idx_map[val].add(len(self.values) - 1)
        return len(self.idx_map[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx_map[val]:
            return False
        remove_idx = self.idx_map[val].pop()
        last_val = self.values[-1]
        self.values[remove_idx] = last_val
        if self.idx_map[last_val]:
            self.idx_map[last_val].add(remove_idx)
            self.idx_map[last_val].discard(len(self.values) - 1)
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)