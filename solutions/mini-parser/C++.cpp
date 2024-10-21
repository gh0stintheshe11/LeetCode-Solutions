class Solution {
public:
    NestedInteger deserialize(string s) {
        if (s.empty()) return NestedInteger();
        if (s[0] != '[') return NestedInteger(stoi(s));

        stack<NestedInteger> stk;
        NestedInteger current;
        int number = 0;
        bool isNegative = false;
        for (size_t i = 0; i < s.size(); ++i) {
            char ch = s[i];

            if (ch == '-') {
                isNegative = true;
            } else if (isdigit(ch)) {
                number = number * 10 + (ch - '0');
            } else if (ch == '[') {
                stk.push(NestedInteger());
            } else if (ch == ',' || ch == ']') {
                if (isdigit(s[i - 1])) {
                    if (isNegative) number = -number;
                    stk.top().add(NestedInteger(number));
                }
                if (ch == ']') {
                    NestedInteger completed = stk.top();
                    stk.pop();
                    if (!stk.empty()) {
                        stk.top().add(completed);
                    } else {
                        return completed;
                    }
                }
                number = 0;
                isNegative = false;
            }
        }

        return stk.empty() ? current : stk.top();
    }
};