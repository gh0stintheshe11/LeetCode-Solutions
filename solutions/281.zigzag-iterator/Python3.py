class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = []
        if v1:
            self.queue.append(iter(v1))
        if v2:
            self.queue.append(iter(v2))
        self.turn = 0

    def next(self) -> int:
        if self.hasNext():
            current_iter = self.queue.pop(0)
            val = next(current_iter)
            self.queue.append(current_iter)  # put the iterator back at the end
            return val
        return None
    
    def hasNext(self) -> bool:
        while self.queue and not self._hasNextFrontIter():
            self.queue.pop(0)
        return bool(self.queue)
    
    def _hasNextFrontIter(self) -> bool:
        if not self.queue:
            return False
        current_iter = self.queue[0]
        try:
            next_val = next(current_iter)
            self.queue.insert(0, iter([next_val] + list(current_iter)))  # reconstruct the iterator
            return True
        except StopIteration:
            return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())