class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> sumIndexMap;
        int maxLength = 0, sum = 0;
        sumIndexMap[0] = -1;
        
        for (int i = 0; i < nums.size(); ++i) {
            sum += nums[i] == 1 ? 1 : -1;
            if (sumIndexMap.find(sum) != sumIndexMap.end()) {
                maxLength = max(maxLength, i - sumIndexMap[sum]);
            } else {
                sumIndexMap[sum] = i;
            }
        }
        
        return maxLength;
    }
};