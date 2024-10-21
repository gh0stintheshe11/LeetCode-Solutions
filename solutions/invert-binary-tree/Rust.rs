

use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = root.clone() {
            let mut node = node.borrow_mut();
            let left = node.left.clone();
            let right = node.right.clone();
            node.left = Self::invert_tree(right);
            node.right = Self::invert_tree(left);
        }
        root
    }
}
