# Definition for an infinite stream.
# class InfiniteStream:
#     def next(self) -> int:
#         pass
class Solution:
    def findPattern(self, stream: 'InfiniteStream', pattern: List[int]) -> int:
        m = len(pattern)
        buffer = []
        index = 0
        
        while True:
            bit = stream.next()
            buffer.append(bit)
            
            if len(buffer) > m:
                buffer.pop(0)
                index += 1
            
            if buffer == pattern:
                return index