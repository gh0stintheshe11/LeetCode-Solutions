impl Solution {
    pub fn is_bipartite(graph: Vec<Vec<i32>>) -> bool {
        let n = graph.len();
        let mut colors = vec![0; n];

        for i in 0..n {
            if colors[i] == 0 && !Self::dfs(&graph, &mut colors, i, 1) {
                return false;
            }
        }

        true
    }

    fn dfs(graph: &Vec<Vec<i32>>, colors: &mut Vec<i32>, node: usize, color: i32) -> bool {
        colors[node] = color;

        for &neighbor in &graph[node] {
            let neighbor = neighbor as usize;
            if colors[neighbor] == color {
                return false;
            }
            if colors[neighbor] == 0 && !Self::dfs(graph, colors, neighbor, -color) {
                return false;
            }
        }

        true
    }
}