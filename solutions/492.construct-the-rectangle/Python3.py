from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math
        for width in range(int(math.sqrt(area)), 0, -1):
            if area % width == 0:
                length = area // width
                return [length, width]