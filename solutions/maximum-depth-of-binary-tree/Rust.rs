
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            Some(node) => {
                let left_depth = Solution::max_depth(node.borrow().left.clone());
                let right_depth = Solution::max_depth(node.borrow().right.clone());
                1 + left_depth.max(right_depth)
            },
            None => 0,
        }
    }
}