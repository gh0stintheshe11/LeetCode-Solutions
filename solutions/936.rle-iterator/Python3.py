from typing import List

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.index = 0

    def next(self, n: int) -> int:
        while self.index < len(self.encoding) and n > self.encoding[self.index]:
            n -= self.encoding[self.index]
            self.index += 2

        if self.index >= len(self.encoding):
            return -1

        self.encoding[self.index] -= n
        return self.encoding[self.index + 1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)