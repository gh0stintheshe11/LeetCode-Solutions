from typing import List
from sortedcontainers import SortedList

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda x: x[1], reverse=True)
        indexed_queries = [(q[0], q[1], i) for i, q in enumerate(queries)]
        indexed_queries.sort(key=lambda x: x[1], reverse=True)

        results = [-1] * len(queries)
        available_rooms = SortedList()
        
        room_idx = 0
        for preferred, min_size, original_idx in indexed_queries:
            while room_idx < len(rooms) and rooms[room_idx][1] >= min_size:
                available_rooms.add(rooms[room_idx][0])
                room_idx += 1
            
            if available_rooms:
                pos = available_rooms.bisect_left(preferred)
                best_room = None
                
                if pos < len(available_rooms):
                    best_room = available_rooms[pos]

                if pos > 0:
                    closest_left_room = available_rooms[pos - 1]
                    if best_room is None or abs(closest_left_room - preferred) <= abs(best_room - preferred):
                        best_room = closest_left_room
                
                results[original_idx] = best_room

        return results