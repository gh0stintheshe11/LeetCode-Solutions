impl Solution {
    pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let target = (graph.len() - 1) as i32;
        let mut result = Vec::new();
        let mut path = vec![0];
        
        Self::dfs(&graph, 0, target, &mut path, &mut result);
        
        result
    }
    
    fn dfs(graph: &Vec<Vec<i32>>, current: i32, target: i32, path: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
        if current == target {
            result.push(path.clone());
            return;
        }
        
        for &next in &graph[current as usize] {
            path.push(next);
            Self::dfs(graph, next, target, path, result);
            path.pop();
        }
    }
}