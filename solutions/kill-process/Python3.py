class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        from collections import defaultdict, deque
        
        # Create a mapping from parent to children processes
        process_map = defaultdict(list)
        for child, parent in zip(pid, ppid):
            process_map[parent].append(child)
        
        # List for all processes to be killed
        to_kill = []
        # Queue for BFS
        queue = deque([kill])
        
        while queue:
            current = queue.popleft()
            to_kill.append(current)
            for child in process_map[current]:
                queue.append(child)
        
        return to_kill