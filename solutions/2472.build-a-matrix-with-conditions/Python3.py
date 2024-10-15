from typing import List, Dict, Set
from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions: List[List[int]]) -> List[int]:
            graph = defaultdict(list)
            indegree = [0] * (k + 1)

            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1

            queue = deque()
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    queue.append(i)

            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            if len(order) == k:
                return order
            return []

        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)

        if not row_order or not col_order:
            return []

        position_row = {num: i for i, num in enumerate(row_order)}
        position_col = {num: i for i, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r = position_row[num]
            c = position_col[num]
            matrix[r][c] = num

        return matrix