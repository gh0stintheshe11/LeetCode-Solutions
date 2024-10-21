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
    ListNode* insertionSortList(ListNode* head) {
        if (!head) return nullptr;

        ListNode* sorted = new ListNode(0); // Dummy node as placeholder for sorted list
        ListNode* curr = head;

        while (curr) {
            ListNode* prev = sorted;
            // Find the correct position to insert the current node
            while (prev->next && prev->next->val < curr->val) {
                prev = prev->next;
            }

            ListNode* next = curr->next; // Save the next node to be processed
            curr->next = prev->next;
            prev->next = curr;
            curr = next; // Move to the next node
        }

        return sorted->next;
    }
};