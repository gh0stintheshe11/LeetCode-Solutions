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
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<long long, int> prefixSumCount;
        prefixSumCount[0] = 1;
        return dfs(root, targetSum, 0, prefixSumCount);
    }

private:
    int dfs(TreeNode* node, int targetSum, long long currentSum, unordered_map<long long, int>& prefixSumCount) {
        if (!node) {
            return 0;
        }
        
        currentSum += node->val;
        int pathCount = prefixSumCount[currentSum - targetSum];
        prefixSumCount[currentSum]++;
        
        pathCount += dfs(node->left, targetSum, currentSum, prefixSumCount);
        pathCount += dfs(node->right, targetSum, currentSum, prefixSumCount);
        
        prefixSumCount[currentSum]--;
        
        return pathCount;
    }
};