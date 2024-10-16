class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> results;
        if (num.empty()) return results;
        addOperatorsHelper(num, target, 0, 0, 0, "", results);
        return results;
    }
    
private:
    void addOperatorsHelper(const string& num, int target, int pos, long long prevValue, long long currentValue, string expression, vector<string>& results) {
        if (pos == num.size()) {
            if (currentValue == target) {
                results.push_back(expression);
            }
            return;
        }
        
        for (int i = pos; i < num.size(); ++i) {
            // Skip number with leading zero
            if (i != pos && num[pos] == '0') break;
            
            string part = num.substr(pos, i - pos + 1);
            long long partValue = stoll(part);
            
            if (pos == 0) {
                addOperatorsHelper(num, target, i + 1, partValue, partValue, part, results);
            } else {
                addOperatorsHelper(num, target, i + 1, partValue, currentValue + partValue, expression + "+" + part, results);
                addOperatorsHelper(num, target, i + 1, -partValue, currentValue - partValue, expression + "-" + part, results);
                addOperatorsHelper(num, target, i + 1, prevValue * partValue, currentValue - prevValue + prevValue * partValue, expression + "*" + part, results);
            }
        }
    }
};