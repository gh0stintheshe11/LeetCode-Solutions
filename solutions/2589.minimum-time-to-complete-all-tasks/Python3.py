class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # Sort tasks by their ending times
        tasks.sort(key=lambda x: x[1])
        
        time_on = set()
        
        for start, end, duration in tasks:
            current_duration = 0

            # Calculate already scheduled time in the task interval
            for t in range(start, end + 1):
                if t in time_on:
                    current_duration += 1

            # Calculate needed additional time
            needed_time = duration - current_duration

            # Schedule the additional needed time at the latest times possible
            for t in range(end, start - 1, -1):
                if needed_time <= 0:
                    break
                if t not in time_on:
                    time_on.add(t)
                    needed_time -= 1

        return len(time_on)