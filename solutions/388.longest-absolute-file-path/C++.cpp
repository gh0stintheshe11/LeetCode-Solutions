class Solution {
public:
    int lengthLongestPath(string input) {
        vector<int> pathLength(1, 0);
        int maxLength = 0;
        size_t pos = 0;

        while (pos < input.size()) {
            size_t end = input.find('\n', pos);
            if (end == string::npos) end = input.size();

            string line = input.substr(pos, end - pos);

            int level = 0;
            while (line[level] == '\t') level++;

            line = line.substr(level);

            if (line.find('.') != string::npos) {
                maxLength = max(maxLength, pathLength[level] + (int)line.size());
            } else {
                if (pathLength.size() <= level + 1) {
                    pathLength.resize(level + 2, 0);
                }
                pathLength[level + 1] = pathLength[level] + line.size() + 1;
            }

            pos = end + 1;
        }

        return maxLength;
    }
};