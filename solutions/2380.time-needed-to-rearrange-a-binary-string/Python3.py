class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        seconds = 0
        while '01' in s:
            s = s.replace('01', '10')
            seconds += 1
        return seconds