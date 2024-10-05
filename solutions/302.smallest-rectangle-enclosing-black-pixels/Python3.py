from typing import List

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def search_row(image, i, j, topToBottom):
            while i != j:
                m = (i + j) // 2
                if ('1' in image[m]) == topToBottom:
                    j = m
                else:
                    i = m + 1
            return i

        def search_col(image, i, j, top, bottom, leftToRight):
            while i != j:
                m = (i + j) // 2
                if any(image[k][m] == '1' for k in range(top, bottom)) == leftToRight:
                    j = m
                else:
                    i = m + 1
            return i
        
        top = search_row(image, 0, x, True)
        bottom = search_row(image, x + 1, len(image), False)
        left = search_col(image, 0, y, top, bottom, True)
        right = search_col(image, y + 1, len(image[0]), top, bottom, False)
        
        return (right - left) * (bottom - top)