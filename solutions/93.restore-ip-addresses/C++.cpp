class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        int len = s.length();
        if (len < 4 || len > 12) return result;
        
        for (int i = 1; i < len && i < 4; ++i) {
            for (int j = i + 1; j < len && j < i + 4; ++j) {
                for (int k = j + 1; k < len && k < j + 4; ++k) {
                    if (len - k > 3) continue;
                    string s1 = s.substr(0, i);
                    string s2 = s.substr(i, j - i);
                    string s3 = s.substr(j, k - j);
                    string s4 = s.substr(k);
                    if (isValid(s1) && isValid(s2) && isValid(s3) && isValid(s4)) {
                        result.emplace_back(s1 + "." + s2 + "." + s3 + "." + s4);
                    }
                }
            }
        }
        
        return result;
    }

private:
    bool isValid(const string& str) {
        if (str.empty() || str.length() > 3 || 
            (str[0] == '0' && str.length() > 1) || 
            stoi(str) > 255) {
            return false;
        }
        return true;
    }
};