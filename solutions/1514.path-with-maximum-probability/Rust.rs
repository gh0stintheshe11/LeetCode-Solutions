use std::collections::{BinaryHeap, HashMap};
use std::cmp::Ordering;

#[derive(Copy, Clone)]
struct State {
    node: i32,
    log_prob: f64,
}

impl PartialEq for State {
    fn eq(&self, other: &Self) -> bool {
        self.node == other.node && (self.log_prob - other.log_prob).abs() < f64::EPSILON
    }
}

impl Eq for State {}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.log_prob.partial_cmp(&self.log_prob).unwrap()
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn max_probability(n: i32, edges: Vec<Vec<i32>>, succ_prob: Vec<f64>, start_node: i32, end_node: i32) -> f64 {
        // Create adjacency list with log probabilities
        let mut graph: HashMap<i32, Vec<(i32, f64)>> = HashMap::new();
        for (edge, &prob) in edges.iter().zip(succ_prob.iter()) {
            let log_prob = -prob.ln(); // Negate for Dijkstra's algorithm
            graph.entry(edge[0]).or_insert(Vec::new()).push((edge[1], log_prob));
            graph.entry(edge[1]).or_insert(Vec::new()).push((edge[0], log_prob));
        }
        
        // Initialize log probabilities
        let mut log_probs = vec![f64::INFINITY; n as usize];
        log_probs[start_node as usize] = 0.0;
        
        // Initialize priority queue
        let mut pq = BinaryHeap::new();
        pq.push(State { node: start_node, log_prob: 0.0 });
        
        while let Some(State { node, log_prob }) = pq.pop() {
            if node == end_node {
                return (-log_prob).exp();
            }
            
            // If we've found a path with lower probability, skip
            if log_prob > log_probs[node as usize] {
                continue;
            }
            
            // Check all neighboring nodes
            if let Some(neighbors) = graph.get(&node) {
                for &(next_node, edge_log_prob) in neighbors {
                    let next_log_prob = log_prob + edge_log_prob;
                    if next_log_prob < log_probs[next_node as usize] {
                        log_probs[next_node as usize] = next_log_prob;
                        pq.push(State { node: next_node, log_prob: next_log_prob });
                    }
                }
            }
        }
        
        0.0 // If we can't reach the end node
    }
}