class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        int n = words.size();
        int index = 0;

        while (index < n) {
            int totalChars = words[index].size();
            int last = index + 1;
            
            while (last < n) {
                if (totalChars + words[last].size() + (last - index) > maxWidth) break;
                totalChars += words[last].size();
                last++;
            }

            string line;
            int numWords = last - index;
            int numSpaces = maxWidth - totalChars;

            if (last == n || numWords == 1) {
                for (int i = index; i < last; ++i) {
                    line += words[i];
                    if (i < last - 1) {
                        line += " ";
                    }
                }
                line += string(maxWidth - line.size(), ' ');
            } else {
                int spacesPerSlot = numSpaces / (numWords - 1);
                int extraSpaces = numSpaces % (numWords - 1);
                
                for (int i = index; i < last; ++i) {
                    line += words[i];
                    if (i < last - 1) {
                        int spaces = spacesPerSlot + (extraSpaces-- > 0 ? 1 : 0);
                        line += string(spaces, ' ');
                    }
                }
            }

            res.push_back(line);
            index = last;
        }
        
        return res;
    }
};