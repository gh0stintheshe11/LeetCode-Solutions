// Definition for singly-linked list.
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
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        use std::collections::VecDeque;

        let mut stack1 = VecDeque::new();
        let mut stack2 = VecDeque::new();

        let mut current = l1;
        while let Some(node) = current {
            stack1.push_back(node.val);
            current = node.next;
        }

        current = l2;
        while let Some(node) = current {
            stack2.push_back(node.val);
            current = node.next;
        }

        let mut carry = 0;
        let mut result: Option<Box<ListNode>> = None;

        while !stack1.is_empty() || !stack2.is_empty() || carry != 0 {
            let sum = carry
                + stack1.pop_back().unwrap_or(0)
                + stack2.pop_back().unwrap_or(0);

            carry = sum / 10;
            let new_node = Box::new(ListNode {
                val: sum % 10,
                next: result,
            });
            result = Some(new_node);
        }

        result
    }
}