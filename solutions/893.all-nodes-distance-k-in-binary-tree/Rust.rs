use std::rc::Rc;
use std::cell::RefCell;
use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn distance_k(root: Option<Rc<RefCell<TreeNode>>>, target: Option<Rc<RefCell<TreeNode>>>, k: i32) -> Vec<i32> {
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        
        // Step 1: Build the graph
        Self::build_graph(&root, None, &mut graph);
        
        // Step 2: BFS from target
        let target_val = target.unwrap().borrow().val;
        let mut queue = VecDeque::new();
        let mut visited = HashMap::new();
        let mut result = Vec::new();
        
        queue.push_back((target_val, 0));
        visited.insert(target_val, true);
        
        while let Some((node, distance)) = queue.pop_front() {
            if distance == k {
                result.push(node);
            } else if distance < k {
                if let Some(neighbors) = graph.get(&node) {
                    for &neighbor in neighbors {
                        if !visited.contains_key(&neighbor) {
                            queue.push_back((neighbor, distance + 1));
                            visited.insert(neighbor, true);
                        }
                    }
                }
            }
        }
        
        result
    }
    
    fn build_graph(node: &Option<Rc<RefCell<TreeNode>>>, parent: Option<i32>, graph: &mut HashMap<i32, Vec<i32>>) {
        if let Some(n) = node {
            let n = n.borrow();
            let val = n.val;
            
            if let Some(p) = parent {
                graph.entry(val).or_insert(Vec::new()).push(p);
                graph.entry(p).or_insert(Vec::new()).push(val);
            }
            
            if n.left.is_some() {
                graph.entry(val).or_insert(Vec::new()).push(n.left.as_ref().unwrap().borrow().val);
                Self::build_graph(&n.left, Some(val), graph);
            }
            
            if n.right.is_some() {
                graph.entry(val).or_insert(Vec::new()).push(n.right.as_ref().unwrap().borrow().val);
                Self::build_graph(&n.right, Some(val), graph);
            }
        }
    }
}