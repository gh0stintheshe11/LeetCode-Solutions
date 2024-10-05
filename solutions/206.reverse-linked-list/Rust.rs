impl Solution {
    // Recursive solution
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        fn reverse(
            node: Option<Box<ListNode>>,
            prev: Option<Box<ListNode>>,
        ) -> Option<Box<ListNode>> {
            match node {
                Some(mut current) => {
                    let next = current.next.take();
                    current.next = prev;
                    reverse(next, Some(current))
                }
                None => prev,
            }
        }
        
        reverse(head, None)
    }
}