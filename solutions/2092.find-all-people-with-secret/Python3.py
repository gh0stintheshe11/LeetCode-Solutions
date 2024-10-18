class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        from collections import defaultdict, deque
        
        meetings.sort(key=lambda x: x[2])
        time_groups = defaultdict(list)
        
        for x, y, time in meetings:
            time_groups[time].append((x, y))
        
        secret_knowers = {0, firstPerson}
        
        for time in sorted(time_groups.keys()):
            current_meetings = time_groups[time]
            graph = defaultdict(list)
            people_set = set()
            
            for x, y in current_meetings:
                graph[x].append(y)
                graph[y].append(x)
                people_set.add(x)
                people_set.add(y)
            
            queue = deque([p for p in people_set if p in secret_knowers])
            local_known = set(queue)
            
            while queue:
                person_with_secret = queue.popleft()
                for peer in graph[person_with_secret]:
                    if peer not in local_known:
                        local_known.add(peer)
                        queue.append(peer)
            
            secret_knowers.update(local_known)
        
        return list(secret_knowers)