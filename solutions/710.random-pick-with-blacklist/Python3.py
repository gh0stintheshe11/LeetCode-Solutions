import random

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        self.blacklist = set(blacklist)
        self.mapping = {}
        self.range_size = n - len(blacklist)
        
        # Map blacklisted indices in the range [0, range_size-1] to valid indices
        blacklist_in_range = {b for b in blacklist if b < self.range_size}
        whitelist_out_of_range = iter(range(self.range_size, n))
        
        for b in blacklist_in_range:
            while True:
                w = next(whitelist_out_of_range)
                if w not in self.blacklist:
                    break
            self.mapping[b] = w

    def pick(self) -> int:
        idx = random.randint(0, self.range_size - 1)
        return self.mapping.get(idx, idx)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()