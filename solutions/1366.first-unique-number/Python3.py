from collections import OrderedDict
from typing import List

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique = OrderedDict()
        self.seen = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        for num in self.unique:
            return num
        return -1

    def add(self, value: int) -> None:
        if value in self.seen:
            if value in self.unique:
                del self.unique[value]
        else:
            self.seen.add(value)
            self.unique[value] = None