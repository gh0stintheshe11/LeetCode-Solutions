from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def canFinish(maxTime: int) -> bool:
            workers = [0] * k
            return dfs(0, workers, maxTime)

        def dfs(jobIndex: int, workers: List[int], maxTime: int) -> bool:
            if jobIndex == len(jobs):
                return True
            currentJob = jobs[jobIndex]
            for i in range(k):
                if workers[i] + currentJob <= maxTime:
                    workers[i] += currentJob
                    if dfs(jobIndex + 1, workers, maxTime):
                        return True
                    workers[i] -= currentJob
                if workers[i] == 0:
                    break
            return False
        
        jobs.sort(reverse=True)
        low, high = max(jobs), sum(jobs)
        
        while low < high:
            mid = (low + high) // 2
            if canFinish(mid):
                high = mid
            else:
                low = mid + 1
        
        return low