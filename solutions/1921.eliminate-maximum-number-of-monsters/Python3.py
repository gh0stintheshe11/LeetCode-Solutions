class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = sorted(d // s + (1 if d % s != 0 else 0) for d, s in zip(dist, speed))
        for minute, time in enumerate(times):
            if time <= minute:
                return minute
        return len(times)