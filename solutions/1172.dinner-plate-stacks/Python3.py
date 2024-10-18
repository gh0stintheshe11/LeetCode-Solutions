from heapq import heappush, heappop

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []  # This will hold all stacks
        self.available = []  # Min-heap to get leftmost available stack with space
        
    def push(self, val: int) -> None:
        # Clean up the available heap to remove outdated indices
        while self.available and (self.available[0] >= len(self.stacks) or len(self.stacks[self.available[0]]) == self.capacity):
            heappop(self.available)
        
        # If there is an available stack, push the value
        if self.available:
            idx = self.available[0]
            self.stacks[idx].append(val)
        else:
            # Otherwise, add a new stack
            self.stacks.append([val])
            idx = len(self.stacks) - 1
        
        # If the stack is not full, add to the available heap
        if len(self.stacks[idx]) < self.capacity:
            heappush(self.available, idx)
        
    def pop(self) -> int:
        # Pop from the rightmost non-empty stack
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        if not self.stacks:
            return -1
        
        result = self.stacks[-1].pop()
        
        if len(self.stacks[-1]) < self.capacity:
            heappush(self.available, len(self.stacks) - 1)
        
        return result

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        
        result = self.stacks[index].pop()
        
        if len(self.stacks[index]) < self.capacity:
            heappush(self.available, index)
        
        return result