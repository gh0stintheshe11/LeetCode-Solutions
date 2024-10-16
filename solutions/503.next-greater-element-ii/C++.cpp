class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, -1);
        stack<int> stk;
        
        for (int i = 0; i < 2 * n; ++i) {
            while (!stk.empty() && nums[stk.top()] < nums[i % n]) {
                result[stk.top()] = nums[i % n];
                stk.pop();
            }
            if (i < n) stk.push(i);
        }
        
        return result;
    }
};