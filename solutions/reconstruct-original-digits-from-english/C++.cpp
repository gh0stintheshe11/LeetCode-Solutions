class Solution {
public:
    string originalDigits(string s) {
        vector<int> count(10, 0);
        vector<int> letters(26, 0);
        
        for (char c : s) {
            letters[c - 'a']++;
        }
        
        // Unique letters for each digit
        count[0] = letters['z' - 'a'];
        count[2] = letters['w' - 'a'];
        count[4] = letters['u' - 'a'];
        count[6] = letters['x' - 'a'];
        count[8] = letters['g' - 'a'];
        
        // Letters that show up in more than one representation
        count[1] = letters['o' - 'a'] - count[0] - count[2] - count[4];
        count[3] = letters['h' - 'a'] - count[8];
        count[5] = letters['f' - 'a'] - count[4];
        count[7] = letters['s' - 'a'] - count[6];
        count[9] = letters['i' - 'a'] - count[5] - count[6] - count[8];
        
        string result;
        for (int i = 0; i < 10; i++) {
            result.append(count[i], '0' + i);
        }
        
        return result;
    }
};