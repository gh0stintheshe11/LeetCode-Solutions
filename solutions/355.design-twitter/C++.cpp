#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using namespace std;

class Twitter {
    int timeStamp;
    unordered_map<int, vector<pair<int, int>>> tweets; // userId -> list of (timeStamp, tweetId)
    unordered_map<int, unordered_set<int>> following; // userId -> set of followed userIds

public:
    Twitter() : timeStamp(0) {
    }
    
    void postTweet(int userId, int tweetId) {
        tweets[userId].emplace_back(timeStamp++, tweetId);
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<int> res;
        priority_queue<pair<int, int>> pq; // (-timeStamp, tweetId) to get max timeStamp first

        // Add user's own tweets
        for (auto& tweet : tweets[userId]) {
            pq.emplace(-tweet.first, tweet.second);
            if (pq.size() > 10)
                pq.pop();
        }

        // Add tweets from following users
        for (int followeeId : following[userId]) {
            if (followeeId == userId) continue; // Skip self-loop
            for (auto& tweet : tweets[followeeId]) {
                pq.emplace(-tweet.first, tweet.second);
                if (pq.size() > 10)
                    pq.pop();
            }
        }

        while (!pq.empty()) {
            res.push_back(pq.top().second);
            pq.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
    
    void follow(int followerId, int followeeId) {
        following[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        following[followerId].erase(followeeId);
    }
};