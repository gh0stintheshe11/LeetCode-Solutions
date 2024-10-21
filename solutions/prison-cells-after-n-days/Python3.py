class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def nextDay(cells):
            return [0] + [1 if cells[i-1] == cells[i+1] else 0 for i in range(1, 7)] + [0]
        
        seen = {}
        while n > 0:
            c = tuple(cells)
            if c in seen:
                n %= seen[c] - n
            seen[c] = n

            if n > 0:
                n -= 1
                cells = nextDay(cells)
        
        return cells