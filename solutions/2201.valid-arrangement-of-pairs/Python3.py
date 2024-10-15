from collections import defaultdict, deque
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        start_node = pairs[0][0]
        for node in out_degree:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break

        def eulerian_path(start):
            stack = [start]
            path = []
            while stack:
                while graph[stack[-1]]:
                    next_node = graph[stack[-1]].popleft()
                    stack.append(next_node)
                path.append(stack.pop())
            return path[::-1]

        path = eulerian_path(start_node)

        result = []
        for i in range(len(path) - 1):
            result.append([path[i], path[i + 1]])

        return result