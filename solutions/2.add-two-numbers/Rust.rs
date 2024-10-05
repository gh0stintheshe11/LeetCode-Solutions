// Definition for singly-linked list.
// Provided by LeetCode, do not redefine in your submission.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }


impl Solution {
    /// Adds two numbers represented by linked lists and returns the sum as a linked list.
    ///
    /// # Arguments
    ///
    /// * `l1` - The first linked list.
    /// * `l2` - The second linked list.
    ///
    /// # Returns
    ///
    /// * A linked list representing the sum of the two numbers.
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        // Initialize a dummy head to simplify edge cases.
        let mut dummy_head = Box::new(ListNode::new(0));
        let mut current = &mut dummy_head;
        let mut p = l1;
        let mut q = l2;
        let mut carry = 0;

        // Traverse both lists until both are exhausted and no carry remains.
        while p.is_some() || q.is_some() || carry != 0 {
            // Extract the current values. If the list has ended, use 0.
            let x = match &p {
                Some(node) => node.val,
                None => 0,
            };
            let y = match &q {
                Some(node) => node.val,
                None => 0,
            };

            // Calculate the sum and update the carry.
            let sum = x + y + carry;
            carry = sum / 10;

            // Create a new node with the digit value.
            current.next = Some(Box::new(ListNode::new(sum % 10)));

            // Move the current pointer.
            current = current.next.as_mut().unwrap();

            // Move to the next nodes in l1 and l2.
            p = match p {
                Some(node) => node.next,
                None => None,
            };
            q = match q {
                Some(node) => node.next,
                None => None,
            };
        }

        // The result is in dummy_head.next
        dummy_head.next
    }
}