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
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        vector<int> path;
        dfs(root, targetSum, path, result);
        return result;
    }
    
private:
    void dfs(TreeNode* node, int targetSum, vector<int>& path, vector<vector<int>>& result) {
        if (!node) return;
        
        path.push_back(node->val);
        
        if (!node->left && !node->right && node->val == targetSum) {
            result.push_back(path);
        }
        
        dfs(node->left, targetSum - node->val, path, result);
        dfs(node->right, targetSum - node->val, path, result);
        
        path.pop_back();
    }
};