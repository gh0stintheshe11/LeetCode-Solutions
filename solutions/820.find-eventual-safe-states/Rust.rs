impl Solution {
    pub fn eventual_safe_nodes(graph: Vec<Vec<i32>>) -> Vec<i32> {
        let n = graph.len();
        let mut safe = vec![None; n];
        let mut result = Vec::new();

        for i in 0..n {
            if Self::is_safe(&graph, i, &mut safe) {
                result.push(i as i32);
            }
        }

        result
    }

    fn is_safe(graph: &Vec<Vec<i32>>, node: usize, safe: &mut Vec<Option<bool>>) -> bool {
        if let Some(is_safe) = safe[node] {
            return is_safe;
        }

        // Mark as unsafe temporarily to detect cycles
        safe[node] = Some(false);

        for &next in &graph[node] {
            if !Self::is_safe(graph, next as usize, safe) {
                return false;
            }
        }

        // If all paths are safe, mark this node as safe
        safe[node] = Some(true);
        true
    }
}