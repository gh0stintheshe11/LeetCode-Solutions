from collections import deque, defaultdict
from typing import List

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # Use BFS to find friends at the requested level
        q = deque([id])
        visited = [False] * len(friends)
        visited[id] = True
        
        # Perform BFS to reach the desired level
        current_level = 0
        while q and current_level < level:
            for _ in range(len(q)):
                current = q.popleft()
                for friend in friends[current]:
                    if not visited[friend]:
                        visited[friend] = True
                        q.append(friend)
            current_level += 1
        
        # At this point, q contains all friends at the desired level
        video_count = defaultdict(int)
        while q:
            friend_id = q.popleft()
            for video in watchedVideos[friend_id]:
                video_count[video] += 1
        
        # Sort the videos by the frequency and then alphabetically
        result = sorted(video_count.keys(), key=lambda x: (video_count[x], x))
        
        return result