class Solution {
public:
    string getHint(string secret, string guess) {
        int bulls = 0, cows = 0;
        int counts[10] = {0};
        
        for (int i = 0; i < secret.size(); ++i) {
            if (secret[i] == guess[i]) {
                ++bulls;
            } else {
                if (counts[secret[i] - '0']++ < 0) ++cows;
                if (counts[guess[i] - '0']-- > 0) ++cows;
            }
        }
        
        return to_string(bulls) + "A" + to_string(cows) + "B";
    }
};