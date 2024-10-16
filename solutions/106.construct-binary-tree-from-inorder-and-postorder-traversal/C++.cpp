/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr, right(nullptr)) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size();
        unordered_map<int, int> inorderIndexMap;
        for (int i = 0; i < n; ++i) {
            inorderIndexMap[inorder[i]] = i;
        }
        return buildSubTree(inorderIndexMap, postorder, 0, n - 1, 0, n - 1);
    }

private:
    TreeNode* buildSubTree(const unordered_map<int, int>& inorderIndexMap,
                           const vector<int>& postorder,
                           int inStart, int inEnd,
                           int postStart, int postEnd) {
        if (inStart > inEnd || postStart > postEnd) {
            return nullptr;
        }

        int rootVal = postorder[postEnd];
        TreeNode* root = new TreeNode(rootVal);
        int rootIndexInInorder = inorderIndexMap.at(rootVal);

        int leftTreeSize = rootIndexInInorder - inStart;
        root->left = buildSubTree(inorderIndexMap, postorder, inStart, rootIndexInInorder - 1, postStart, postStart + leftTreeSize - 1);
        root->right = buildSubTree(inorderIndexMap, postorder, rootIndexInInorder + 1, inEnd, postStart + leftTreeSize, postEnd - 1);

        return root;
    }
};