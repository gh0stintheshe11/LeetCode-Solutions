class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> nextGreaterMap;
        stack<int> s;
        
        for (int i = 0; i < nums2.size(); ++i) {
            while (!s.empty() && nums2[i] > s.top()) {
                nextGreaterMap[s.top()] = nums2[i];
                s.pop();
            }
            s.push(nums2[i]);
        }
        
        while (!s.empty()) {
            nextGreaterMap[s.top()] = -1;
            s.pop();
        }
        
        vector<int> result;
        for (int num : nums1) {
            result.push_back(nextGreaterMap[num]);
        }
        
        return result;
    }
};