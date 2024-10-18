impl Solution {
    pub fn maximal_network_rank(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut adj_matrix = vec![vec![false; n]; n];
        let mut degrees = vec![0; n];

        // Build adjacency matrix and count degrees
        for road in &roads {
            let (a, b) = (road[0] as usize, road[1] as usize);
            adj_matrix[a][b] = true;
            adj_matrix[b][a] = true;
            degrees[a] += 1;
            degrees[b] += 1;
        }

        let mut max_rank = 0;

        // Check all pairs of cities
        for i in 0..n {
            for j in (i + 1)..n {
                let mut rank = degrees[i] + degrees[j];
                // If there's a direct road between i and j, subtract 1
                if adj_matrix[i][j] {
                    rank -= 1;
                }
                max_rank = max_rank.max(rank);
            }
        }

        max_rank
    }
}