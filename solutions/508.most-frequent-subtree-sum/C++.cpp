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
    vector<int> findFrequentTreeSum(TreeNode* root) {
        unordered_map<int, int> sumFrequency;
        int maxFrequency = 0;
        calculateSubtreeSums(root, sumFrequency, maxFrequency);

        vector<int> result;
        for (auto& [sum, frequency] : sumFrequency) {
            if (frequency == maxFrequency) {
                result.push_back(sum);
            }
        }
        
        return result;
    }
    
private:
    int calculateSubtreeSums(TreeNode* node, unordered_map<int, int>& sumFrequency, int& maxFrequency) {
        if (!node) return 0;
        
        int leftSum = calculateSubtreeSums(node->left, sumFrequency, maxFrequency);
        int rightSum = calculateSubtreeSums(node->right, sumFrequency, maxFrequency);
        int totalSum = node->val + leftSum + rightSum;
        
        sumFrequency[totalSum]++;
        maxFrequency = max(maxFrequency, sumFrequency[totalSum]);
        
        return totalSum;
    }
};