from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(start <= queryTime <= end for start, end in zip(startTime, endTime))