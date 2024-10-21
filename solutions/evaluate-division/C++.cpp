class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, unordered_map<string, double>> graph;

        for (int i = 0; i < equations.size(); ++i) {
            const auto& eq = equations[i];
            const double value = values[i];
            graph[eq[0]][eq[1]] = value;
            graph[eq[1]][eq[0]] = 1.0 / value;
        }

        vector<double> results;
        for (const auto& query : queries) {
            const auto& start = query[0];
            const auto& end = query[1];
            if (!graph.count(start) || !graph.count(end)) {
                results.push_back(-1.0);
            } else if (start == end) {
                results.push_back(1.0);
            } else {
                unordered_set<string> visited;
                double result = dfs(graph, start, end, visited);
                results.push_back(result);
            }
        }

        return results;
    }

private:
    double dfs(unordered_map<string, unordered_map<string, double>>& graph, const string& start, const string& end, unordered_set<string>& visited) {
        if (graph[start].count(end)) {
            return graph[start][end];
        }
        
        visited.insert(start);

        for (const auto& neighbor : graph[start]) {
            if (!visited.count(neighbor.first)) {
                double result = dfs(graph, neighbor.first, end, visited);
                if (result != -1.0) {
                    return neighbor.second * result;
                }
            }
        }

        return -1.0;
    }
};