class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> subsequence;
        backtrack(nums, 0, subsequence, result);
        return result;
    }
    
private:
    void backtrack(vector<int>& nums, int start, vector<int>& subsequence, vector<vector<int>>& result) {
        if (subsequence.size() >= 2) {
            result.push_back(subsequence);
        }
        unordered_set<int> used;
        for (int i = start; i < nums.size(); ++i) {
            if ((subsequence.empty() || nums[i] >= subsequence.back()) && used.find(nums[i]) == used.end()) {
                used.insert(nums[i]);
                subsequence.push_back(nums[i]);
                backtrack(nums, i + 1, subsequence, result);
                subsequence.pop_back();
            }
        }
    }
};