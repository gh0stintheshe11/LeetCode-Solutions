use std::collections::VecDeque;

impl Solution {
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let n = num_courses as usize;
        let mut graph = vec![Vec::new(); n];
        let mut in_degree = vec![0; n];
        
        // Build the graph and calculate in-degrees
        for prereq in prerequisites {
            let (course, prerequisite) = (prereq[0] as usize, prereq[1] as usize);
            graph[prerequisite].push(course);
            in_degree[course] += 1;
        }
        
        // Initialize queue with all nodes that have no incoming edges
        let mut queue = VecDeque::new();
        for i in 0..n {
            if in_degree[i] == 0 {
                queue.push_back(i);
            }
        }
        
        let mut order = Vec::new();
        
        // Process the queue
        while let Some(node) = queue.pop_front() {
            order.push(node as i32);
            
            // Reduce in-degree of adjacent nodes
            for &neighbor in &graph[node] {
                in_degree[neighbor] -= 1;
                if in_degree[neighbor] == 0 {
                    queue.push_back(neighbor);
                }
            }
        }
        
        // Check if topological sort is possible
        if order.len() == n {
            order
        } else {
            Vec::new()
        }
    }
}