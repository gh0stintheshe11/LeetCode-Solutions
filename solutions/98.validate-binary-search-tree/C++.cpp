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
    bool isValidBST(TreeNode* root) {
        return validate(root, nullptr, nullptr);
    }
    
private:
    bool validate(TreeNode* node, TreeNode* minNode, TreeNode* maxNode) {
        if (!node) return true;
        if ((minNode && node->val <= minNode->val) || (maxNode && node->val >= maxNode->val)) {
            return false;
        }
        return validate(node->left, minNode, node) && validate(node->right, node, maxNode);
    }
};