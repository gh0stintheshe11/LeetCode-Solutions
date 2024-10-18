class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        return max((job + worker - 1) // worker for job, worker in zip(jobs, workers))