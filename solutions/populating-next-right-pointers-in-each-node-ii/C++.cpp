/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        Node* head = root; // head of the current level

        while (head != nullptr) {
            Node* dummy = new Node(); // dummy node for the next level
            Node* tail = dummy; // tail for the next level
            Node* current = head; // traverse the current level
            
            while (current != nullptr) {
                if (current->left) {
                    tail->next = current->left;
                    tail = tail->next;
                }
                if (current->right) {
                    tail->next = current->right;
                    tail = tail->next;
                }
                current = current->next;
            }
            
            head = dummy->next; // move to the next level
            delete dummy; // clean up dummy node
        }

        return root;
    }
};