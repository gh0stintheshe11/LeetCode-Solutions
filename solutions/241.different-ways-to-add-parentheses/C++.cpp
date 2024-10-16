class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        vector<int> ans;
        for (int i = 0; i < expression.size(); ++i) {
            if (expression[i] == '+' || expression[i] == '-' || expression[i] == '*') {
                vector<int> left = diffWaysToCompute(expression.substr(0, i));
                vector<int> right = diffWaysToCompute(expression.substr(i + 1));
                for (int l : left) {
                    for (int r : right) {
                        if (expression[i] == '+') {
                            ans.push_back(l + r);
                        } else if (expression[i] == '-') {
                            ans.push_back(l - r);
                        } else if (expression[i] == '*') {
                            ans.push_back(l * r);
                        }
                    }
                }
            }
        }
        if (ans.empty()) {
            ans.push_back(stoi(expression));
        }
        return ans;
    }
};