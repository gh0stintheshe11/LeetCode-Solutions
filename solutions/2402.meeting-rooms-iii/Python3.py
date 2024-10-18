from heapq import heappop, heappush
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # Sort meetings based on start times
        
        # Min-heap for available rooms, initially all rooms are available
        available_rooms = list(range(n))
        
        # Min-heap for ongoing meetings (end time, room number)
        ongoing_meetings = []
        
        # Room usage count
        room_count = [0] * n
        
        for start, end in meetings:
            # Free up rooms that have their meetings ended by the start time
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                end_time, room = heappop(ongoing_meetings)
                heappush(available_rooms, room)
            
            # Assign a room to the current meeting
            if available_rooms:
                # If there's an available room, choose the one with the smallest number
                room = heappop(available_rooms)
                heappush(ongoing_meetings, (end, room))
            else:
                # If no rooms are available, delay this meeting to the earliest possible time
                end_time_soonest, room = heappop(ongoing_meetings)
                duration = end - start
                end_time_new = end_time_soonest + duration
                heappush(ongoing_meetings, (end_time_new, room))
            
            # Record the meeting in the chosen room
            room_count[room] += 1
        
        # Find the room with the most meetings, and in case of a tie, the smallest room number
        max_meetings = max(room_count)
        for i in range(n):
            if room_count[i] == max_meetings:
                return i