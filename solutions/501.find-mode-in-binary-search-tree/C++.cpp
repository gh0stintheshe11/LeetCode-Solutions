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
private:
    TreeNode* prev = nullptr;
    int maxCount = 0;
    int currentCount = 0;
    vector<int> modes;
    
    void inorder(TreeNode* node) {
        if (!node) return;
        inorder(node->left);
        handleValue(node->val);
        inorder(node->right);
    }
    
    void handleValue(int val) {
        if (prev != nullptr && prev->val == val) {
            currentCount++;
        } else {
            currentCount = 1;
        }
        
        if (currentCount > maxCount) {
            maxCount = currentCount;
            modes = {val};
        } else if (currentCount == maxCount) {
            modes.push_back(val);
        }
        
        prev = new TreeNode(val);  // Update prev to the current node's value
    }
    
public:
    vector<int> findMode(TreeNode* root) {
        inorder(root);
        return modes;
    }
};