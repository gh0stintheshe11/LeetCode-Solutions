class Solution:
    def countPoints(self, rings: str) -> int:
        rod_colors = [set() for _ in range(10)]
        
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod_index = int(rings[i+1])
            rod_colors[rod_index].add(color)
        
        return sum(1 for colors in rod_colors if len(colors) == 3)