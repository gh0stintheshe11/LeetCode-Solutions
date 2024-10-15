from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isReachable = [[False] * numCourses for _ in range(numCourses)]
        
        for pre, course in prerequisites:
            isReachable[pre][course] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    isReachable[i][j] = isReachable[i][j] or (isReachable[i][k] and isReachable[k][j])
        
        return [isReachable[u][v] for u, v in queries]