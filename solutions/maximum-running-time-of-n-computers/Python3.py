class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def canRunFor(minutes: int) -> bool:
            total_power = 0
            for battery in batteries:
                total_power += min(battery, minutes)
            return total_power >= n * minutes

        batteries.sort()
        left, right = 1, sum(batteries) // n

        while left < right:
            mid = (right + left + 1) // 2
            if canRunFor(mid):
                left = mid
            else:
                right = mid - 1
        
        return left