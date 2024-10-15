from typing import List

class VideoSharingPlatform:

    def __init__(self):
        self.videos = {}
        self.available_ids = set()
        self.next_id = 0

    def upload(self, video: str) -> int:
        if self.available_ids:
            vid_id = self.available_ids.pop()
        else:
            vid_id = self.next_id
            self.next_id += 1
        self.videos[vid_id] = {'content': video, 'views': 0, 'likes': 0, 'dislikes': 0}
        return vid_id

    def remove(self, videoId: int) -> None:
        if videoId in self.videos:
            del self.videos[videoId]
            self.available_ids.add(videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.videos:
            return "-1"
        video = self.videos[videoId]['content']
        self.videos[videoId]['views'] += 1
        return video[startMinute:min(endMinute + 1, len(video))]

    def like(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId]['likes'] += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId]['dislikes'] += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId not in self.videos:
            return [-1]
        video = self.videos[videoId]
        return [video['likes'], video['dislikes']]

    def getViews(self, videoId: int) -> int:
        if videoId not in self.videos:
            return -1
        return self.videos[videoId]['views']