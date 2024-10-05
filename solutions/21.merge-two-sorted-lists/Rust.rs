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
    pub fn merge_two_lists(
        list1: Option<Box<ListNode>>,
        list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        // Create a dummy node to act as the start of the merged list
        let mut dummy = ListNode::new(0);
        // Create a mutable reference to the current node in the merged list
        let mut current = &mut dummy;

        // Create mutable references to the heads of the input lists
        let mut l1 = list1;
        let mut l2 = list2;

        // Loop until one of the lists is exhausted
        while let (Some(n1), Some(n2)) = (l1.as_ref(), l2.as_ref()) {
            if n1.val <= n2.val {
                // Move the node from list1 to the merged list
                current.next = l1;
                current = current.next.as_mut().unwrap();
                l1 = current.next.take();
            } else {
                // Move the node from list2 to the merged list
                current.next = l2;
                current = current.next.as_mut().unwrap();
                l2 = current.next.take();
            }
        }

        // Attach the remaining nodes from the non-exhausted list
        current.next = if l1.is_some() { l1 } else { l2 };

        // Return the merged list, skipping the dummy node
        dummy.next
    }
}
