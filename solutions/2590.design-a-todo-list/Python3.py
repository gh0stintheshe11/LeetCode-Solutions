from collections import defaultdict
from typing import List

class TodoList:
    
    def __init__(self):
        self.user_tasks = defaultdict(list)  # { userId: [(taskId, dueDate, taskDescription, completed, tags)] }
        self.current_task_id = 1

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        task = (self.current_task_id, dueDate, taskDescription, False, tags)
        self.user_tasks[userId].append(task)
        self.current_task_id += 1
        return task[0]

    def getAllTasks(self, userId: int) -> List[str]:
        tasks = sorted(
            (task for task in self.user_tasks[userId] if not task[3]), 
            key=lambda x: x[1]
        )
        return [task[2] for task in tasks]

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        tasks = sorted(
            (task for task in self.user_tasks[userId] if not task[3] and tag in task[4]), 
            key=lambda x: x[1]
        )
        return [task[2] for task in tasks]

    def completeTask(self, userId: int, taskId: int) -> None:
        for i, (tid, dueDate, desc, completed, tags) in enumerate(self.user_tasks[userId]):
            if tid == taskId and not completed:
                self.user_tasks[userId][i] = (tid, dueDate, desc, True, tags)
                break