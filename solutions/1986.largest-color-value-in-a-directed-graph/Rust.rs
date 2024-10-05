use std::collections::{VecDeque, HashMap};

impl Solution {
    pub fn largest_path_value(colors: String, edges: Vec<Vec<i32>>) -> i32 {
        let n = colors.len();
        let colors: Vec<u8> = colors.bytes().map(|c| c - b'a').collect();
        
        // Build adjacency list and in-degree count
        let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
        let mut in_degree = vec![0; n];
        for edge in edges {
            let (u, v) = (edge[0] as usize, edge[1] as usize);
            graph[u].push(v);
            in_degree[v] += 1;
        }
        
        // Initialize queue for topological sort
        let mut queue = VecDeque::new();
        for i in 0..n {
            if in_degree[i] == 0 {
                queue.push_back(i);
            }
        }
        
        // Initialize DP table
        let mut dp = vec![vec![0; 26]; n];
        let mut visited = 0;
        let mut max_color_value = 0;
        
        // Perform topological sort and update DP
        while let Some(u) = queue.pop_front() {
            visited += 1;
            dp[u][colors[u] as usize] += 1;
            max_color_value = max_color_value.max(*dp[u].iter().max().unwrap());
            
            for &v in &graph[u] {
                for c in 0..26 {
                    dp[v][c] = dp[v][c].max(dp[u][c]);
                }
                in_degree[v] -= 1;
                if in_degree[v] == 0 {
                    queue.push_back(v);
                }
            }
        }
        
        // Check if there's a cycle
        if visited != n {
            -1
        } else {
            max_color_value
        }
    }
}