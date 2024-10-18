from collections import deque
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        in_degree = [0] * n
        graph = [[] for _ in range(n)]
        
        for u, v in relations:
            graph[u-1].append(v-1)
            in_degree[v-1] += 1
        
        queue = deque()
        earliest_completion = [0] * n
        
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
                earliest_completion[i] = time[i]
        
        while queue:
            course = queue.popleft()
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                earliest_completion[next_course] = max(earliest_completion[next_course],
                                                       earliest_completion[course] + time[next_course])
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return max(earliest_completion)