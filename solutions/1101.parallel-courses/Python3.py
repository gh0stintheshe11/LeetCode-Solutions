from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0] * (n + 1)

        for pre, next in relations:
            graph[pre].append(next)
            indegree[next] += 1

        queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])
        semesters = 0
        courses_taken = 0

        while queue:
            for _ in range(len(queue)):
                course = queue.popleft()
                courses_taken += 1
                for neighbor in graph[course]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            semesters += 1

        return semesters if courses_taken == n else -1