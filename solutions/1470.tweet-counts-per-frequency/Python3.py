from collections import defaultdict
from typing import List

class TweetCounts:

    def __init__(self):
        self.tweet_records = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweet_records[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        frequencies = {"minute": 60, "hour": 3600, "day": 86400}
        interval = frequencies[freq]
        time_buckets = (endTime - startTime) // interval + 1
        counts = [0] * time_buckets
        
        for time in self.tweet_records[tweetName]:
            if startTime <= time <= endTime:
                index = (time - startTime) // interval
                counts[index] += 1
                
        return counts