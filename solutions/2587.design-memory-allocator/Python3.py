class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n
        self.blocks = {}

    def allocate(self, size: int, mID: int) -> int:
        consecutive_free = 0
        start_idx = -1
        
        for i in range(len(self.memory)):
            if self.memory[i] == 0:
                consecutive_free += 1
                if consecutive_free == size:
                    start_idx = i - size + 1
                    for j in range(start_idx, start_idx + size):
                        self.memory[j] = mID
                    if mID not in self.blocks:
                        self.blocks[mID] = 0
                    self.blocks[mID] += size
                    return start_idx
            else:
                consecutive_free = 0
        
        return -1

    def free(self, mID: int) -> int:
        if mID not in self.blocks:
            return 0
        freed_units = 0
        
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                self.memory[i] = 0
                freed_units += 1
        
        del self.blocks[mID]
        
        return freed_units