class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def can_assign(n):
            task_i = 0
            task_temp = deque()
            n_pills = pills
            for i in range(n-1,-1,-1):
                while task_i < n and tasks[task_i] <= workers[i]+strength:
                    task_temp.append(tasks[task_i])
                    task_i += 1
                
                if len(task_temp) == 0:
                    return False
                if workers[i] >= task_temp[0]:
                    task_temp.popleft()
                elif n_pills > 0:
                    task_temp.pop()
                    n_pills -= 1
                else:
                    return False
            return True
        
        tasks.sort()
        workers.sort(reverse = True)
        
        l = 0
        r = min(len(tasks), len(workers))
        res = -1
        while l <= r:
            m = (l+r)//2
            if can_assign(m):
                res = m
                l = m+1
            else:
                r = m-1
        return res