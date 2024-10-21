#include <vector>
#include <string>
#include <stack>

class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        std::stack<int> stk;
        for (const std::string& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int b = stk.top(); stk.pop();
                int a = stk.top(); stk.pop();
                if (token == "+") stk.push(a + b);
                if (token == "-") stk.push(a - b);
                if (token == "*") stk.push(a * b);
                if (token == "/") stk.push(a / b);
            } else {
                stk.push(std::stoi(token));
            }
        }
        return stk.top();
    }
};