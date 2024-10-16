class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> combination;
        backtrack(1, n, k, combination, result);
        return result;
    }

private:
    void backtrack(int start, int n, int k, vector<int>& combination, vector<vector<int>>& result) {
        if (k == 0) {
            result.push_back(combination);
            return;
        }
        for (int i = start; i <= n; ++i) {
            combination.push_back(i);
            backtrack(i + 1, n, k - 1, combination, result);
            combination.pop_back();
        }
    }
};