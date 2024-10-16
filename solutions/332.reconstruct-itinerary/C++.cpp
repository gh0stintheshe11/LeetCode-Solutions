#include <vector>
#include <string>
#include <unordered_map>
#include <map>
#include <deque>

using namespace std;

class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, multiset<string>> graph;
        vector<string> result;
        for (const vector<string>& ticket : tickets) {
            graph[ticket[0]].insert(ticket[1]);
        }
        
        deque<string> stack;
        stack.push_back("JFK");
        
        while (!stack.empty()) {
            string cur = stack.back();
            if (graph[cur].empty()) {
                result.push_back(cur);
                stack.pop_back();
            } else {
                stack.push_back(*graph[cur].begin());
                graph[cur].erase(graph[cur].begin());
            }
        }
        
        reverse(result.begin(), result.end());
        return result;
    }
};