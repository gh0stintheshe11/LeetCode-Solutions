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
    void recoverTree(TreeNode* root) {
        TreeNode *first = nullptr, *second = nullptr, *prev = nullptr;
        
        TreeNode* cur = root;
        while (cur) {
            if (cur->left == nullptr) {
                // Check the current node
                if (prev && prev->val > cur->val) {
                    if (!first) {
                        first = prev;
                    }
                    second = cur;
                }
                prev = cur;
                cur = cur->right;
            } else {
                TreeNode* pred = cur->left;
                while (pred->right && pred->right != cur) {
                    pred = pred->right;
                }
                
                if (!pred->right) {
                    pred->right = cur;
                    cur = cur->left;
                } else {
                    pred->right = nullptr;
                    if (prev && prev->val > cur->val) {
                        if (!first) {
                            first = prev;
                        }
                        second = cur;
                    }
                    prev = cur;
                    cur = cur->right;
                }
            }
        }
        
        if (first && second) {
            std::swap(first->val, second->val);
        }
    }
};