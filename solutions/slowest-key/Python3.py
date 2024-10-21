class Solution:
    def slowestKey(self, releaseTimes: list, keysPressed: str) -> str:
        max_duration = releaseTimes[0]
        slowest_key = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > max_duration or (duration == max_duration and keysPressed[i] > slowest_key):
                max_duration = duration
                slowest_key = keysPressed[i]

        return slowest_key