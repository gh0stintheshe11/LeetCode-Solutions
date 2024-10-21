/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* first = head;
        ListNode* second = head;
        ListNode* kthFromBegin = nullptr;
        
        // Move `first` to the kth node from start
        for (int i = 1; i < k; ++i) {
            first = first->next;
        }
        
        // kthFromBegin is now the kth node from start
        kthFromBegin = first;
        
        // Move `first` to the end, moving `second` such that it reaches the kth node from the end
        first = first->next;
        
        while (first) {
            first = first->next;
            second = second->next;
        }
        
        // Swap the values of the kth node from the beginning and kth node from the end
        std::swap(kthFromBegin->val, second->val);
        
        return head;
    }
};