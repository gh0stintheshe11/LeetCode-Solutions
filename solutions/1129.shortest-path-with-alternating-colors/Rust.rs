use std::collections::VecDeque;

impl Solution {
    pub fn shortest_alternating_paths(n: i32, red_edges: Vec<Vec<i32>>, blue_edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut graph = vec![vec![vec![]; 2]; n];
        
        // Build the graph
        for edge in red_edges {
            graph[edge[0] as usize][0].push(edge[1] as usize);
        }
        for edge in blue_edges {
            graph[edge[0] as usize][1].push(edge[1] as usize);
        }
        
        let mut distances = vec![-1; n];
        let mut visited = vec![vec![false; 2]; n];
        let mut queue = VecDeque::new();
        
        // Start BFS from node 0
        queue.push_back((0, 0, 0)); // (node, color, distance)
        queue.push_back((0, 1, 0));
        distances[0] = 0;
        
        while let Some((node, color, dist)) = queue.pop_front() {
            if visited[node][color] {
                continue;
            }
            visited[node][color] = true;
            
            if distances[node] == -1 || dist < distances[node] {
                distances[node] = dist;
            }
            
            let next_color = 1 - color;
            for &next_node in &graph[node][next_color] {
                if !visited[next_node][next_color] {
                    queue.push_back((next_node, next_color, dist + 1));
                }
            }
        }
        
        distances
    }
}