from typing import List
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        arrivals = sorted((times[i][0], i) for i in range(n))
        departs = [(times[i][1], i) for i in range(n)]
        heapq.heapify(departs)

        free_chairs = []
        occupied_chairs = {}
        available_chair = 0

        for arrival_time, friend in arrivals:
            while departs and departs[0][0] <= arrival_time:
                depart_time, departing_friend = heapq.heappop(departs)
                heapq.heappush(free_chairs, occupied_chairs.pop(departing_friend))

            if free_chairs:
                chair = heapq.heappop(free_chairs)
            else:
                chair = available_chair
                available_chair += 1

            occupied_chairs[friend] = chair

            if friend == targetFriend:
                return chair