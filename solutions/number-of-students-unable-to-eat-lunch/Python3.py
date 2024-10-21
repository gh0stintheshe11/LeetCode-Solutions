class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        
        queue = deque(students)
        stack = deque(sandwiches)
        
        consecutive_passes = 0
        while queue and consecutive_passes < len(queue):
            if queue[0] == stack[0]:
                queue.popleft()
                stack.popleft()
                consecutive_passes = 0
            else:
                queue.append(queue.popleft())
                consecutive_passes += 1
        
        return len(queue)