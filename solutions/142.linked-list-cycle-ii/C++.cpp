/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head || !head->next) return nullptr;

        ListNode *slow = head, *fast = head;

        // Detect if there is a cycle in the linked list
        do {
            if (!fast || !fast->next) return nullptr;
            slow = slow->next;
            fast = fast->next->next;
        } while (slow != fast);

        // Find the starting node of the cycle
        slow = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }

        return slow;
    }
};