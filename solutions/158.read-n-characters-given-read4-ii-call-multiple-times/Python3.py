# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.queue = []
    
    def read(self, buf: List[str], n: int) -> int:
        idx = 0
        while idx < n:
            if not self.queue:
                buf4 = [''] * 4
                count = read4(buf4)
                if count == 0:
                    break
                self.queue.extend(buf4[:count])

            buf[idx] = self.queue.pop(0)
            idx += 1
        
        return idx