from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        graph = defaultdict(list)
        for i, num in enumerate(arr):
            graph[num].append(i)

        queue = deque([0])
        visited = {0}
        steps = 0

        while queue:
            steps += 1
            for _ in range(len(queue)):
                index = queue.popleft()

                # Check neighboring indices
                for neighbor in (index - 1, index + 1):
                    if 0 <= neighbor < len(arr) and neighbor not in visited:
                        if neighbor == len(arr) - 1:
                            return steps
                        visited.add(neighbor)
                        queue.append(neighbor)

                # Check same value indices
                while graph[arr[index]]:
                    neighbor = graph[arr[index]].pop()
                    if neighbor not in visited:
                        if neighbor == len(arr) - 1:
                            return steps
                        visited.add(neighbor)
                        queue.append(neighbor)

        return steps