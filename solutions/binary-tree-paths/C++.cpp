/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> paths;
        if (root == nullptr) return paths;
        findPaths(root, "", paths);
        return paths;
    }
    
    void findPaths(TreeNode* node, string path, vector<string>& paths) {
        if (node == nullptr) return;
        path += to_string(node->val);
        if (node->left == nullptr && node->right == nullptr) {
            paths.push_back(path);
        } else {
            path += "->";
            findPaths(node->left, path, paths);
            findPaths(node->right, path, paths);
        }
    }
};