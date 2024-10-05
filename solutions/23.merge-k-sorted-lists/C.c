/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    // Dummy node to serve as the start of the merged list
    struct ListNode dummy;
    dummy.next = NULL;
    struct ListNode* tail = &dummy;

    // Merge the two lists
    while (l1 != NULL && l2 != NULL) {
        if (l1->val <= l2->val) {
            tail->next = l1;  // Attach l1 node
            l1 = l1->next;    // Move l1 forward
        } else {
            tail->next = l2;  // Attach l2 node
            l2 = l2->next;    // Move l2 forward
        }
        tail = tail->next;    // Move tail forward
    }

    // Attach the remaining nodes, if any
    if (l1 != NULL) {
        tail->next = l1;
    } else if (l2 != NULL) {
        tail->next = l2;
    }

    return dummy.next;  // Return the merged list starting from dummy.next
}

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    if (listsSize == 0) {
        return NULL;
    }

    int interval = 1;
    // Continue merging lists in pairs
    while (interval < listsSize) {
        for (int i = 0; i + interval < listsSize; i += interval * 2) {
            // Merge lists[i] and lists[i + interval] and store the result back in lists[i]
            lists[i] = mergeTwoLists(lists[i], lists[i + interval]);
        }
        interval *= 2;  // Increase the interval
    }

    return lists[0];  // The merged list will be at lists[0]
}
