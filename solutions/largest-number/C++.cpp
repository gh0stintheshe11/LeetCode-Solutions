class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> numStrings;
        for (int num : nums) {
            numStrings.push_back(to_string(num));
        }

        sort(numStrings.begin(), numStrings.end(), [](const string &a, const string &b) {
            return a + b > b + a;
        });

        if (numStrings[0] == "0") {
            return "0";
        }

        string largestNum = "";
        for (const string &numStr : numStrings) {
            largestNum += numStr;
        }

        return largestNum;
    }
};