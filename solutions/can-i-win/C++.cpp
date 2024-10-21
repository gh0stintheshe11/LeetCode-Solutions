class Solution {
public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        if (desiredTotal == 0) return true;
        if (maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal) return false;
        
        std::vector<int> dp(1 << maxChoosableInteger, -1);
        return canWin(maxChoosableInteger, desiredTotal, 0, dp);
    }

private:
    bool canWin(int maxChoosable, int desiredTotal, int used, std::vector<int>& dp) {
        if (dp[used] != -1) return dp[used];
        
        for (int i = 0; i < maxChoosable; ++i) {
            if (!(used & (1 << i))) {
                int newTotal = desiredTotal - (i + 1);
                if (newTotal <= 0 || !canWin(maxChoosable, newTotal, used | (1 << i), dp)) {
                    return dp[used] = 1;
                }
            }
        }
        
        return dp[used] = 0;
    }
};