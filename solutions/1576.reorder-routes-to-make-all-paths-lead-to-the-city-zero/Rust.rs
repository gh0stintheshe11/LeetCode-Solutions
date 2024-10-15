use std::collections::{HashSet, HashMap};

impl Solution {
    pub fn min_reorder(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut original_directions: HashSet<(i32, i32)> = HashSet::new();
        
        // Build the graph and record original directions
        for connection in &connections {
            let (a, b) = (connection[0], connection[1]);
            graph.entry(a).or_insert(Vec::new()).push(b);
            graph.entry(b).or_insert(Vec::new()).push(a);
            original_directions.insert((a, b));
        }
        
        let mut visited: HashSet<i32> = HashSet::new();
        
        // DFS function
        fn dfs(node: i32, parent: i32, graph: &HashMap<i32, Vec<i32>>, 
               original_directions: &HashSet<(i32, i32)>, visited: &mut HashSet<i32>) -> i32 {
            let mut count = 0;
            visited.insert(node);
            
            if let Some(neighbors) = graph.get(&node) {
                for &neighbor in neighbors {
                    if !visited.contains(&neighbor) {
                        if original_directions.contains(&(node, neighbor)) {
                            count += 1;
                        }
                        count += dfs(neighbor, node, graph, original_directions, visited);
                    }
                }
            }
            
            count
        }
        
        dfs(0, -1, &graph, &original_directions, &mut visited)
    }
}