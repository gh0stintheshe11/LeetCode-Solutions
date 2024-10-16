class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        int index = 0;
        int i = 0;
        
        while (i < n) {
            char currentChar = chars[i];
            int count = 0;
            
            while (i < n && chars[i] == currentChar) {
                i++;
                count++;
            }
            
            chars[index++] = currentChar;
            if (count > 1) {
                string countStr = to_string(count);
                for (char c : countStr) {
                    chars[index++] = c;
                }
            }
        }
        
        return index;
    }
};