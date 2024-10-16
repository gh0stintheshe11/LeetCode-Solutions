/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;
        
        // Step 1: Weave original list with copied nodes
        Node* curr = head;
        while (curr) {
            Node* copy = new Node(curr->val);
            copy->next = curr->next;
            curr->next = copy;
            curr = copy->next;
        }
        
        // Step 2: Assign random pointers for the copied nodes
        curr = head;
        while (curr) {
            if (curr->random) {
                curr->next->random = curr->random->next;
            }
            curr = curr->next->next;
        }
        
        // Step 3: Unweave to restore original list and extract the copied list
        curr = head;
        Node* pseudoHead = new Node(0);
        Node* copyCurr = pseudoHead;
        
        while (curr) {
            Node* nextOrig = curr->next->next;
            // Extract the copy
            copyCurr->next = curr->next;
            copyCurr = copyCurr->next;
            // Restore the original list
            curr->next = nextOrig;
            
            curr = nextOrig;
        }
        
        return pseudoHead->next;
    }
};