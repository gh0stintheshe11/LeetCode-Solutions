from typing import List
from collections import deque

class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        result = [-1] * n
        entry_queue = deque()
        exit_queue = deque()
        
        i = 0
        current_time = 0
        last_action = -1  # -1: no action, 0: entry, 1: exit
        
        while i < n or entry_queue or exit_queue:
            while i < n and arrival[i] <= current_time:
                if state[i] == 0:
                    entry_queue.append(i)
                else:
                    exit_queue.append(i)
                i += 1
            
            if exit_queue and (last_action == 1 or not entry_queue or last_action == -1):
                person = exit_queue.popleft()
                last_action = 1
            elif entry_queue:
                person = entry_queue.popleft()
                last_action = 0
            else:
                last_action = -1
                current_time += 1
                continue
            
            result[person] = current_time
            current_time += 1
        
        return result