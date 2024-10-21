#include <string>
#include <vector>

class Solution {
public:
    std::string simplifyPath(std::string path) {
        std::vector<std::string> stack;
        int i = 0;
        
        while (i < path.size()) {
            // Skip the initial slashes to find the directory or command
            while (i < path.size() && path[i] == '/') i++;
            if (i == path.size()) break;

            int j = i;
            while (j < path.size() && path[j] != '/') j++;
            std::string part = path.substr(i, j - i);

            if (part == "..") {
                if (!stack.empty()) stack.pop_back();
            } else if (part != ".") {
                stack.push_back(part);
            }
            
            i = j;
        }

        std::string result = "/";
        for (int k = 0; k < stack.size(); k++) {
            result += stack[k];
            if (k < stack.size() - 1) result += "/";
        }
        
        return result;
    }
};