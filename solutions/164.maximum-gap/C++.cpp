#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int maximumGap(std::vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;
        
        int minValue = *std::min_element(nums.begin(), nums.end());
        int maxValue = *std::max_element(nums.begin(), nums.end());
        
        if (maxValue == minValue) return 0;
        
        int bucketSize = std::max(1, (maxValue - minValue) / (n - 1));
        int bucketCount = (maxValue - minValue) / bucketSize + 1;
        
        std::vector<int> minBucket(bucketCount, INT_MAX);
        std::vector<int> maxBucket(bucketCount, INT_MIN);
        
        for (int num : nums) {
            int bucketIndex = (num - minValue) / bucketSize;
            minBucket[bucketIndex] = std::min(minBucket[bucketIndex], num);
            maxBucket[bucketIndex] = std::max(maxBucket[bucketIndex], num);
        }
        
        int maxGap = 0;
        int previousMax = minValue;
        
        for (int i = 0; i < bucketCount; ++i) {
            if (minBucket[i] == INT_MAX) continue;
            maxGap = std::max(maxGap, minBucket[i] - previousMax);
            previousMax = maxBucket[i];
        }
        
        return maxGap;
    }
};