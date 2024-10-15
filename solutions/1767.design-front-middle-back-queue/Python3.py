from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.front_half = deque()
        self.back_half = deque()

    def rebalance(self):
        # Ensure that front_half has either the same number of elements as back_half or one more
        if len(self.front_half) > len(self.back_half) + 1:
            self.back_half.appendleft(self.front_half.pop())
        elif len(self.front_half) < len(self.back_half):
            self.front_half.append(self.back_half.popleft())

    def pushFront(self, val: int) -> None:
        self.front_half.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front_half) > len(self.back_half):
            self.back_half.appendleft(self.front_half.pop())
        self.front_half.append(val)
        self.rebalance()

    def pushBack(self, val: int) -> None:
        self.back_half.append(val)
        self.rebalance()

    def popFront(self) -> int:
        if not self.front_half and not self.back_half:
            return -1
        if self.front_half:
            val = self.front_half.popleft()
        else:
            val = self.back_half.popleft()
        self.rebalance()
        return val

    def popMiddle(self) -> int:
        if not self.front_half and not self.back_half:
            return -1
        if len(self.front_half) == len(self.back_half):
            val = self.front_half.pop()
        else:
            val = self.front_half.pop()
        self.rebalance()
        return val

    def popBack(self) -> int:
        if not self.front_half and not self.back_half:
            return -1
        if self.back_half:
            val = self.back_half.pop()
        else:
            val = self.front_half.pop()
        self.rebalance()
        return val