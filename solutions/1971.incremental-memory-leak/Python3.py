class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        t = 1
        while memory1 >= t or memory2 >= t:
            if memory1 >= memory2:
                memory1 -= t
            else:
                memory2 -= t
            t += 1
        return [t, memory1, memory2]