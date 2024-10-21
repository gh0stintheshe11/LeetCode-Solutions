#include <unordered_map>
#include <vector>
#include <algorithm>

class Solution {
public:
    string frequencySort(string s) {
        std::unordered_map<char, int> frequency;
        
        for (char c : s) {
            frequency[c]++;
        }
        
        std::vector<std::pair<char, int>> freqVec(frequency.begin(), frequency.end());
        
        std::sort(freqVec.begin(), freqVec.end(), [](const std::pair<char, int>& a, const std::pair<char, int>& b) {
            return a.second > b.second;
        });
        
        std::string result;
        result.reserve(s.size());
        
        for (const auto& pair : freqVec) {
            result.append(pair.second, pair.first);
        }
        
        return result;
    }
};