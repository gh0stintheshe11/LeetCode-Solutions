class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Define the binary search range
        left, right = 1, int(1e18)
        result = right

        # Perform binary search
        while left <= right:
            mid = left + (right - left) // 2

            # Check if we can reduce the mountain within 'mid' seconds
            if self.canReduceMountain(mountainHeight, workerTimes, mid):
                result = mid  # Mid is a valid time, try for a smaller time
                right = mid - 1
            else:
                left = mid + 1  # Mid is too small, try a larger time

        return result

    # Helper function to check if the mountain can be reduced within the given time
    def canReduceMountain(self, mountainHeight: int, workerTimes: List[int], timeLimit: int) -> bool:
        totalHeightReduced = 0

        # For each worker, calculate how much height they can reduce within the timeLimit
        for time in workerTimes:
            maxUnits = 0
            left, right = 1, mountainHeight

            # Binary search to find the max units this worker can reduce within timeLimit
            while left <= right:
                mid = left + (right - left) // 2
                requiredTime = time * mid * (mid + 1) // 2  # Time required for the worker to reduce 'mid' units

                if requiredTime <= timeLimit:
                    maxUnits = mid  # If the worker can reduce 'mid' units within timeLimit
                    left = mid + 1  # Try to find more units
                else:
                    right = mid - 1  # Otherwise, try for fewer units

            totalHeightReduced += maxUnits
            if totalHeightReduced >= mountainHeight:
                return True  # If total height reduced exceeds or equals the mountain's height

        return totalHeightReduced >= mountainHeight