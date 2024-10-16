class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unordered_map<int, int> sumMap;
        int count = 0;
        
        for (int a : nums1) {
            for (int b : nums2) {
                sumMap[a + b]++;
            }
        }
        
        for (int c : nums3) {
            for (int d : nums4) {
                int target = -(c + d);
                if (sumMap.find(target) != sumMap.end()) {
                    count += sumMap[target];
                }
            }
        }
        
        return count;
    }
};