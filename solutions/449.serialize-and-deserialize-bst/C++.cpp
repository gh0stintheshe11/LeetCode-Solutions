#include <string>
#include <sstream>
#include <vector>

using namespace std;

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string result;
        preorder(root, result);
        return result;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        vector<int> values;
        stringstream ss(data);
        string token;
        while (getline(ss, token, ',')) {
            if (!token.empty()) {
                values.push_back(stoi(token));
            }
        }
        int index = 0;
        return buildTree(values, index, INT_MIN, INT_MAX);
    }

private:
    void preorder(TreeNode* node, string& result) {
        if (!node) return;
        result += to_string(node->val) + ",";
        preorder(node->left, result);
        preorder(node->right, result);
    }

    TreeNode* buildTree(vector<int>& values, int& index, int lower, int upper) {
        if (index >= values.size()) return nullptr;
        int value = values[index];
        if (value < lower || value > upper) return nullptr;
        index++;
        TreeNode* node = new TreeNode(value);
        node->left = buildTree(values, index, lower, value);
        node->right = buildTree(values, index, value, upper);
        return node;
    }
};