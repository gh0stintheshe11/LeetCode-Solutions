from typing import List
from collections import defaultdict

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creator_views = defaultdict(int)
        creator_videos = defaultdict(list)

        for creator, vid_id, view in zip(creators, ids, views):
            creator_views[creator] += view
            creator_videos[creator].append((-view, vid_id))
        
        max_popularity = max(creator_views.values())
        result = []

        for creator in creator_views:
            if creator_views[creator] == max_popularity:
                result.append([creator, min(creator_videos[creator])[1]])
        
        return result