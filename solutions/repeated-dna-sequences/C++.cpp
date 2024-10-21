class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<string, int> sequenceCount;
        vector<string> result;
        
        if (s.length() < 10) return result;

        for (int i = 0; i <= s.length() - 10; ++i) {
            string sequence = s.substr(i, 10);
            sequenceCount[sequence]++;
        }
        
        for (auto& pair : sequenceCount) {
            if (pair.second > 1) {
                result.push_back(pair.first);
            }
        }
        
        return result;
    }
};