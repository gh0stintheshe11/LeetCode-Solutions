use std::collections::HashMap;

impl Solution {
    pub fn critical_connections(n: i32, connections: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for connection in &connections {
            graph.entry(connection[0]).or_insert(Vec::new()).push(connection[1]);
            graph.entry(connection[1]).or_insert(Vec::new()).push(connection[0]);
        }

        let mut low = vec![0; n as usize];
        let mut disc = vec![-1; n as usize];
        let mut parent = vec![-1; n as usize];
        let mut time = 0;
        let mut result = Vec::new();

        for i in 0..n {
            if disc[i as usize] == -1 {
                Self::dfs(i, &mut time, &graph, &mut low, &mut disc, &mut parent, &mut result);
            }
        }

        result
    }

    fn dfs(u: i32, time: &mut i32, graph: &HashMap<i32, Vec<i32>>, 
           low: &mut Vec<i32>, disc: &mut Vec<i32>, parent: &mut Vec<i32>, 
           result: &mut Vec<Vec<i32>>) {
        disc[u as usize] = *time;
        low[u as usize] = *time;
        *time += 1;

        if let Some(neighbors) = graph.get(&u) {
            for &v in neighbors {
                if disc[v as usize] == -1 {
                    parent[v as usize] = u;
                    Self::dfs(v, time, graph, low, disc, parent, result);

                    low[u as usize] = low[u as usize].min(low[v as usize]);

                    if low[v as usize] > disc[u as usize] {
                        result.push(vec![u, v]);
                    }
                } else if v != parent[u as usize] {
                    low[u as usize] = low[u as usize].min(disc[v as usize]);
                }
            }
        }
    }
}