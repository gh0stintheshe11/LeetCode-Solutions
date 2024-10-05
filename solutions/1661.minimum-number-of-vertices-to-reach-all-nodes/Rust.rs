use std::collections::HashSet;

impl Solution {
    pub fn find_smallest_set_of_vertices(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        // Create a set of all nodes
        let mut nodes: HashSet<i32> = (0..n).collect();

        // Remove nodes that have incoming edges
        for edge in edges {
            nodes.remove(&edge[1]);
        }

        // Convert the remaining nodes to a vector
        nodes.into_iter().collect()
    }
}