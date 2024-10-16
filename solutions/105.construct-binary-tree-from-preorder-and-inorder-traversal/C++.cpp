#include <vector>
#include <unordered_map>

using namespace std;

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> inorder_map;
        for (int i = 0; i < inorder.size(); ++i) {
            inorder_map[inorder[i]] = i;
        }
        int preorder_index = 0;
        return buildTreeHelper(preorder, inorder_map, preorder_index, 0, inorder.size() - 1);
    }
    
private:
    TreeNode* buildTreeHelper(const vector<int>& preorder, const unordered_map<int, int>& inorder_map, 
                              int& preorder_index, int left, int right) {
        if (left > right) {
            return nullptr;
        }
        
        int root_val = preorder[preorder_index];
        TreeNode* root = new TreeNode(root_val);
        
        ++preorder_index;
        
        root->left = buildTreeHelper(preorder, inorder_map, preorder_index, left, inorder_map.at(root_val) - 1);
        root->right = buildTreeHelper(preorder, inorder_map, preorder_index, inorder_map.at(root_val) + 1, right);

        return root;
    }
};