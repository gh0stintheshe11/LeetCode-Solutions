import heapq
from collections import defaultdict, deque
from typing import List

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(deque)   # userId -> deque of (timestamp, tweetId)
        self.followees = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        recent_tweets = list(self.tweets[userId])
        for followeeId in self.followees[userId]:
            recent_tweets.extend(self.tweets[followeeId])
        
        # Get the 10 most recent tweets
        most_recent_tweets = heapq.nlargest(10, recent_tweets, key=lambda x: x[0])
        return [tweetId for timestamp, tweetId in most_recent_tweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)