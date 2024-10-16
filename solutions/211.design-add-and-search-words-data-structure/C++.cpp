class WordDictionary {
private:
    struct TrieNode {
        TrieNode* children[26];
        bool isEndOfWord;
        TrieNode() : isEndOfWord(false) {
            for (int i = 0; i < 26; ++i) children[i] = nullptr;
        }
    };
    
    TrieNode* root;

    bool searchInNode(const string& word, TrieNode* node, int index) {
        if (index == word.size()) return node->isEndOfWord;
        
        char c = word[index];
        if (c == '.') {
            for (int i = 0; i < 26; ++i) {
                if (node->children[i] && searchInNode(word, node->children[i], index + 1))
                    return true;
            }
            return false;
        } else {
            int idx = c - 'a';
            if (!node->children[idx]) return false;
            return searchInNode(word, node->children[idx], index + 1);
        }
    }
    
public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* node = root;
        for (char c : word) {
            int index = c - 'a';
            if (!node->children[index]) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
        }
        node->isEndOfWord = true;
    }
    
    bool search(string word) {
        return searchInNode(word, root, 0);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */