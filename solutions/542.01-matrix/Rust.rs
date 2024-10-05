use std::collections::VecDeque;

impl Solution {
    pub fn update_matrix(mat: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let (m, n) = (mat.len(), mat[0].len());
        let mut result = vec![vec![-1; n]; m];
        let mut queue = VecDeque::new();
        
        // Initialize the queue with all 0s and mark them in the result
        for i in 0..m {
            for j in 0..n {
                if mat[i][j] == 0 {
                    result[i][j] = 0;
                    queue.push_back((i, j));
                }
            }
        }
        
        // BFS
        let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        while let Some((i, j)) = queue.pop_front() {
            for (di, dj) in &directions {
                let ni = i as i32 + di;
                let nj = j as i32 + dj;
                if ni >= 0 && ni < m as i32 && nj >= 0 && nj < n as i32 {
                    let ni = ni as usize;
                    let nj = nj as usize;
                    if result[ni][nj] == -1 {
                        result[ni][nj] = result[i][j] + 1;
                        queue.push_back((ni, nj));
                    }
                }
            }
        }
        
        result
    }
}