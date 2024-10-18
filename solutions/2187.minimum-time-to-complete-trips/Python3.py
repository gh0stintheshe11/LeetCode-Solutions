class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def trips_in_time(t):
            return sum(t // bus_time for bus_time in time)
        
        left, right = 1, min(time) * totalTrips
        while left < right:
            mid = (left + right) // 2
            if trips_in_time(mid) >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return left