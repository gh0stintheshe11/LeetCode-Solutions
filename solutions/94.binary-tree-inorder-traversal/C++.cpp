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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> stk;
        TreeNode* current = root;
        
        while (current != nullptr || !stk.empty()) {
            while (current != nullptr) {
                stk.push(current);
                current = current->left;
            }
            current = stk.top();
            stk.pop();
            result.push_back(current->val);
            current = current->right;
        }
        
        return result;
    }
};