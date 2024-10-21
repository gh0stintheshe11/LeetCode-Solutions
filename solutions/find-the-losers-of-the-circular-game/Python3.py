class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        received = [False] * n
        current = 0
        step = 1
        
        while not received[current]:
            received[current] = True
            current = (current + step * k) % n
            step += 1
        
        return [i + 1 for i in range(n) if not received[i]]