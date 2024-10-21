class Solution {
public:
    bool makesquare(vector<int>& matchsticks) {
        int totalLength = 0;
        for (int match : matchsticks) {
            totalLength += match;
        }

        if (totalLength % 4 != 0) {
            return false;
        }

        int sideLength = totalLength / 4;
        sort(matchsticks.rbegin(), matchsticks.rend());

        vector<int> sides(4, 0);
        return dfs(matchsticks, sides, 0, sideLength);
    }

private:
    bool dfs(vector<int>& matchsticks, vector<int>& sides, int index, int target) {
        if (index == matchsticks.size()) {
            return sides[0] == target && sides[1] == target && sides[2] == target && sides[3] == target;
        }

        for (int i = 0; i < 4; ++i) {
            if (sides[i] + matchsticks[index] > target) {
                continue;
            }

            sides[i] += matchsticks[index];
            if (dfs(matchsticks, sides, index + 1, target)) {
                return true;
            }
            sides[i] -= matchsticks[index];

            if (sides[i] == 0) {
                break;
            }
        }

        return false;
    }
};