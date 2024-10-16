/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr, right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        std::queue<TreeNode*> q;
        q.push(root);
        
        int bottomLeftValue = root->val;
        
        while (!q.empty()) {
            int size = q.size();
            bottomLeftValue = q.front()->val;
            
            for (int i = 0; i < size; ++i) {
                TreeNode* node = q.front();
                q.pop();
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        
        return bottomLeftValue;
    }
};