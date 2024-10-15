from typing import List, Optional

# Definition for an infinite stream.
# class InfiniteStream:
#     def next(self) -> int:
#         pass

class Solution:
    def findPattern(self, stream: Optional['InfiniteStream'], pattern: List[int]) -> int:
        if not pattern:
            return 0
        
        pattern_length = len(pattern)
        current_stream = []

        index = 0
        while True:
            bit = stream.next()
            current_stream.append(bit)
            if len(current_stream) > pattern_length:
                current_stream.pop(0)
            
            if current_stream == pattern:
                return index - pattern_length + 1

            index += 1