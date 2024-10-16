/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string result;
        serializeHelper(root, result);
        return result;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int pos = 0;
        return deserializeHelper(data, pos);
    }

private:
    void serializeHelper(TreeNode* node, string &result) {
        if (!node) {
            result += "null,";
            return;
        }
        
        result += to_string(node->val) + ",";
        serializeHelper(node->left, result);
        serializeHelper(node->right, result);
    }
    
    TreeNode* deserializeHelper(const string &data, int &pos) {
        if (pos >= data.size()) return nullptr;
        
        int nextComma = data.find(',', pos);
        string token = data.substr(pos, nextComma - pos);
        pos = nextComma + 1;

        if (token == "null") {
            return nullptr;
        } else {
            TreeNode* node = new TreeNode(stoi(token));
            node->left = deserializeHelper(data, pos);
            node->right = deserializeHelper(data, pos);
            return node;
        }
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));