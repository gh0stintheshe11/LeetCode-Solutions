/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x, left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class BSTIterator {
private:
    std::stack<TreeNode*> nodeStack;
    
    // Helper function to push all the left children of the node to the stack
    void pushLeftChildren(TreeNode* node) {
        while (node != nullptr) {
            nodeStack.push(node);
            node = node->left;
        }
    }
    
public:
    BSTIterator(TreeNode* root) {
        pushLeftChildren(root);
    }
    
    int next() {
        TreeNode* node = nodeStack.top();
        nodeStack.pop();
        // Since we're moving to the next node, push all the left children of the right child
        if (node->right != nullptr) {
            pushLeftChildren(node->right);
        }
        return node->val;
    }
    
    bool hasNext() {
        return !nodeStack.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */