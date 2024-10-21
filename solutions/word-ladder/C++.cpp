#include <unordered_set>
#include <queue>
#include <string>
#include <vector>

class Solution {
public:
    int ladderLength(std::string beginWord, std::string endWord, std::vector<std::string>& wordList) {
        std::unordered_set<std::string> wordSet(wordList.begin(), wordList.end());
        if (wordSet.find(endWord) == wordSet.end()) return 0;
        
        std::queue<std::string> q;
        q.push(beginWord);
        
        int level = 1;
        
        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; ++i) {
                std::string currentWord = q.front();
                q.pop();
                
                // Try changing each character of currentWord to every lowercase letter
                for (size_t j = 0; j < currentWord.length(); ++j) {
                    char originalChar = currentWord[j];
                    
                    for (char c = 'a'; c <= 'z'; ++c) {
                        if (c == originalChar) continue;
                        currentWord[j] = c;
                        
                        if (currentWord == endWord) {
                            return level + 1;
                        }
                        
                        if (wordSet.find(currentWord) != wordSet.end()) {
                            q.push(currentWord);
                            wordSet.erase(currentWord);
                        }
                    }
                    currentWord[j] = originalChar; // Change back to original character
                }
            }
            ++level;
        }
        
        return 0;
    }
};