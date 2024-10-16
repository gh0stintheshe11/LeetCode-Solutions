class Solution {
public:
    struct TrieNode {
        TrieNode* children[26];
        string word;
        TrieNode() : word("") {
            for (int i = 0; i < 26; ++i) {
                children[i] = nullptr;
            }
        }
    };
    
    void insert(TrieNode* root, const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
        }
        node->word = word;
    }
    
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        // Build Trie from the list of words
        TrieNode* root = new TrieNode();
        for (const string& word : words) {
            insert(root, word);
        }
        
        vector<string> result;
        int m = board.size(), n = board[0].size();
        
        function<void(int, int, TrieNode*)> backtrack = [&](int i, int j, TrieNode* node) {
            char c = board[i][j];
            if (c == '#' || node->children[c - 'a'] == nullptr) return;
            node = node->children[c - 'a'];
            if (!node->word.empty()) {
                result.push_back(node->word);
                node->word.clear(); // avoid duplicates
            }
            
            board[i][j] = '#';
            if (i > 0) backtrack(i - 1, j, node);
            if (j > 0) backtrack(i, j - 1, node);
            if (i < m - 1) backtrack(i + 1, j, node);
            if (j < n - 1) backtrack(i, j + 1, node);
            board[i][j] = c;
        };
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                backtrack(i, j, root);
            }
        }
        
        return result;
    }
};