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
    ListNode* reverseKGroup(ListNode* head, int k) {
        // Check if we have enough nodes to reverse in k-group
        ListNode* node = head;
        for (int i = 0; i < k; ++i) {
            if (!node) return head;
            node = node->next;
        }

        // Reverse k nodes
        ListNode* prev = nullptr;
        ListNode* current = head;
        for (int i = 0; i < k; ++i) {
            ListNode* next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }

        // Recursively reverse the remaining linked list
        head->next = reverseKGroup(current, k);

        // Return the new head after reversal
        return prev;
    }
};