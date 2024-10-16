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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || k == 0)
            return head;

        // First, determine the length of the list and the last node
        int length = 1;
        ListNode* tail = head;
        while (tail->next) {
            tail = tail->next;
            length++;
        }

        // Connect the end of the list to the head making it a circle
        tail->next = head;

        // Calculate the effective number of rotations
        k = k % length;
        int stepsToNewHead = length - k;

        // Find the new tail and break the circle
        ListNode* newTail = tail;
        while (stepsToNewHead--) {
            newTail = newTail->next;
        }

        ListNode* newHead = newTail->next;
        newTail->next = nullptr;

        return newHead;
    }
};