class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        if (k < 0) return 0;
        unordered_map<int, int> numCount;
        for (int num : nums) {
            numCount[num]++;
        }
        
        int count = 0;
        for (auto& pair : numCount) {
            if (k == 0) {
                if (pair.second > 1) count++;
            } else {
                if (numCount.find(pair.first + k) != numCount.end()) count++;
            }
        }
        return count;
    }
};