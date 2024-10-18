from typing import List

class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo: 'FontInfo') -> int:
        def canFit(fontSize):
            totalWidth = sum(fontInfo.getWidth(fontSize, ch) for ch in text)
            return fontInfo.getHeight(fontSize) <= h and totalWidth <= w
        
        left, right = 0, len(fonts) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if canFit(fonts[mid]):
                result = fonts[mid]
                left = mid + 1
            else:
                right = mid - 1
        
        return result