from functools import total_ordering
from heapq import heappop, heappush

@total_ordering
class List:
    def __init__(self, val: int, pos: int, prev: List | None = None, fol: List | None = None):
        self.val = val
        self.prev = prev
        self.fol = fol
        self.pos = pos
        self.alive = True
    
    def __eq__(self, other):
        # type equality missing
        return self.val == other.val and self.pos == other.pos
    
    def __lt__(self, other):
        if self.val > other.val:
            return True
        elif self.val == other.val:
            return self.pos > other.pos
        else:
            return False
        

class MaxStack:

    def __init__(self):
        self.stack = None
        self.heap = []
        

    def push(self, x: int) -> None:
        fol = List(x, self.stack.pos+1 if self.stack else 0, self.stack, None)
        if self.stack is not None:
            self.stack.fol = fol
        self.stack = fol
        heappush(self.heap, fol)

    def pop(self) -> int:
        while not self.stack.alive:
            extracted = self.stack
            self.stack = extracted.prev
        extracted = self.stack
        extracted.alive = False
        self.stack = extracted.prev
        return extracted.val
        

    def top(self) -> int:
        while not self.stack.alive:
            extracted = self.stack
            self.stack = extracted.prev
        return self.stack.val

    def peekMax(self) -> int:
        while not self.heap[0].alive:
            heappop(self.heap)
        return self.heap[0].val
        

    def popMax(self) -> int:
        while not self.heap[0].alive:
            heappop(self.heap)
        top = heappop(self.heap)
        top.alive = False
        return top.val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()