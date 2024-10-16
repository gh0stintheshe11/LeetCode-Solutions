#include <string>
#include <vector>
#include <unordered_set>
#include <queue>

using namespace std;

class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        unordered_set<string> dict(bank.begin(), bank.end());
        if (dict.find(endGene) == dict.end()) return -1;
        
        queue<pair<string, int>> q;
        q.push({startGene, 0});
        vector<char> genes = {'A', 'C', 'G', 'T'};
        
        while (!q.empty()) {
            auto [current, steps] = q.front();
            q.pop();
            
            if (current == endGene) return steps;
            
            for (int i = 0; i < current.size(); ++i) {
                char original = current[i];
                for (char gene : genes) {
                    if (gene == original) continue;

                    current[i] = gene;
                    
                    if (dict.find(current) != dict.end()) {
                        q.push({current, steps + 1});
                        dict.erase(current);
                    }
                }
                current[i] = original;
            }
        }
        
        return -1;
    }
};